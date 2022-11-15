from flask import Flask, request, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage

from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    UserMixin
)
from modules.shared import db, ma

from modules import html_strings
from modules.relations import parts, customer, job_card, staff, equipment
from modules.sanitise import char_check, check_email, check_digits, check_abc123, check_abc123_spaces
from settings import (
    client_id,
    client_secret,
    SQLALCHEMY_DATABASE_URI,
    secret_key
)


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.secret_key = secret_key

# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = OAUTHLIB_INSECURE_TRANSPORT
# os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = OAUTHLIB_RELAX_TOKEN_SCOPE

login_manager = LoginManager()
login_manager.init_app(app)


db.init_app(app)
ma.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).filter(User.id == user_id)).scalar()


class OAuth(OAuthConsumerMixin, db.Model):
    pass


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    profile_pic = db.Column(db.String)


blueprint = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    reprompt_consent=True,
    scope=["profile", "email"]
)

blueprint.storage = SQLAlchemyStorage(OAuth, db.session)

app.register_blueprint(blueprint, url_prefix="/login")


@app.route("/")
def index():
    if current_user.is_authenticated:
        return '<html style="background-color:black"><h1 style="color:white">Welcome to eJobs!</h1>' + html_strings.index_list() + '</html>'

    else:
        google_data = None
        user_info_endpoint = '/oauth2/v2/userinfo'
        if google.authorized:
            google_data = google.get(user_info_endpoint).json()
            print(google_data)
            if not db.session.execute(db.select(User).filter(User.id == google_data['id'])).scalar():
                new_user = User(id=google_data['id'], name=google_data['name'], email=google_data['email'],
                                profile_pic=google_data['picture'])
                db.session.add_all([new_user])
                db.session.commit()

            user = db.session.execute(db.select(User).filter(User.id == google_data['id'])).scalar()
            login_user(user)

        return redirect(url_for("login"))


@app.route('/login')
def login():
    return redirect(url_for('google.login'))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return '<html><body style="text-align:center;margin-top:50vh;background-color:black;color:white;">' \
           + '<h1>Until Next Time!</h1></body></html>'


@app.route('/create_all/')
def create_db_all():
    db.create_all()
    # staff
    stff_seed = staff.staff_seed()
    db.session.add_all(stff_seed)
    # customers
    cstmr_seed = customer.customer_seed()
    db.session.add_all(cstmr_seed)
    # parts
    prt_seed = parts.parts_seed()
    db.session.add_all(prt_seed)
    # equipment
    eqpmnt_seed = equipment.equipment_seed()
    db.session.add_all(eqpmnt_seed)
    # jobs
    jb_seed = job_card.job_seed()
    db.session.add_all(jb_seed)
    db.session.commit()
    print("All Done")
    return '<html style="background-color:black"><h1 style="color:white">All Done!</h1>' + html_strings.index_list() + '</html>'


@app.route('/equipment/all/')
@login_required
def equipment_all():
    return equipment.all_equipment()


@app.route('/equipment/sn/<sn>/')
@login_required
def equip_by_sn(sn):
    return char_check(sn, equipment.get_equip_by_sn(sn))


@app.route('/equipment/customer/<id>/')
@login_required
def equip_by_cust_id(id):
    return char_check(equipment.get_equip_by_cust_id(id))


@app.route('/equipment/new/', methods=['POST'])
@login_required
def equipment_new():
    cust_id = request.form['customer_id']
    sn = request.form['serial_number']
    make = request.form['make']
    model = request.form['model']
    cycle_count = request.form['cycle_count']
    mfy = request.form['mfy']

    if check_abc123([cust_id, sn, make, model]) and check_digits([cycle_count, mfy]):
        return equipment.new_equipment(cust_id, sn, make, model, cycle_count, mfy)
    else:
        return 'Illegal characters entered', 400


@app.route('/customers/all/')
@login_required
def customers_all():
    return customer.all_customers()


@app.route('/customers/id/<id>/')
@login_required
def cust_by_id(id):
    return char_check(id, customer.get_cust_by_id(id))


@app.route('/customer/add_form/')
@login_required
def new_customer():
    return html_strings.cust_template()


@app.route('/customer/new/', methods=['POST'])
@login_required
def customer_add():
    business_name = request.form['business_name']
    branch_name = request.form['branch_name']
    contact_name = request.form['contact_name']
    phone_number = request.form['phone_number']
    email_address = request.form['email_address']
    location = request.form['location']

    if check_abc123_spaces([business_name, branch_name, contact_name]) and \
            check_digits([phone_number]) and check_email([email_address]):
        return customer.add_customer(business_name, branch_name, contact_name, phone_number, email_address, location)
    else:
        return 'Illegal characters entered', 400


@app.route('/jobs/all/')
@login_required
def jobs_all():
    completed = request.args.get('completed')
    return job_card.all_jobs(completed)


@app.route('/jobs/id/<id>/')
@login_required
def job_by_id(id):
    return char_check(id, job_card.get_job_by_id(id))


@app.route('/jobs/add_form/')
@login_required
def new_job():
    return html_strings.make_new_card()


@app.route('/jobs/update/', methods=['POST'])
@login_required
def job_update():
    job_id = request.form['job_id']
    comments = request.form['comments']
    if check_abc123([job_id, comments]):
        return job_card.update_job(job_id, comments)
    else:
        return 'Illegal characters entered', 400


@app.route('/jobs/new/', methods=['POST'])
@login_required
def card_new():
    c = request.form['customer_id']
    issue = request.form['issue']
    machine = request.form['serial_number']
    technician = request.form['staff_id']
    if check_abc123([c, issue, machine, technician]):
        return job_card.new_card(c, issue, machine, technician)
    else:
        return 'Illegal characters entered', 400


@app.route('/parts/all/')
@login_required
def parts_all():
    return parts.all_parts()


@app.route('/parts/number/<pn>/')
@login_required
def parts_by_pn(pn):
    return char_check(pn, parts.get_parts_by_pn(pn))


@app.route('/parts/new/')
@login_required
def new_parts_screen():
    return html_strings.parts_template()


@app.route('/parts/post_part/', methods=['POST'])
@login_required
def post_parts():
    pn = request.form['part_number']
    name = request.form['name']
    quantity = request.form['quantity']
    supplier = request.form['supplier']
    if check_abc123([pn, name, quantity, supplier]):
        return parts.new_parts(name, quantity, supplier, pn)
    else:
        return 'Illegal characters entered', 400


@app.route('/staff/all/')
@login_required
def staff_all():
    return staff.all_staff()


@app.route('/staff/id/<id>/')
@login_required
def staff_by_id(id):
    return char_check(id, staff.get_staff_by_id(id))


@app.route('/staff/delete/<id>/')
@login_required
def staff_delete_by_id(id):
    return char_check(id, staff.delete_staff_by_id(id))


@app.route('/staff/new/', methods=['POST'])
@login_required
def staff_new():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    role = request.form['role']
    phone_number = request.form['phone_number']
    email_address = request.form['email_address']
    if check_abc123([first_name, last_name, role]) and check_digits([phone_number]) and check_email([email_address]):
        return staff.new_staff(first_name, last_name, role, phone_number, email_address)
    else:
        return 'Illegal characters entered', 400


if __name__ == "__main__":
    app.run(port=8000, debug=True)
