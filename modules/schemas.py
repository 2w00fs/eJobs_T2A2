from modules.shared import db, ma


class Jobcard(db.Model):
    __tablename__ = 'job_card'

    job_id = db.Column(db.String, primary_key=True)
    customer_id = db.Column(db.String, db.ForeignKey('customer.customer_id'))
    technician_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))
    machine = db.Column(db.String, db.ForeignKey('equipment.serial_number'))
    issue = db.Column(db.String)
    comments = db.Column(db.String)
    completed = db.Column(db.Boolean)


class JobcardSchema(ma.Schema):
    class Meta:
        fields = ('job_id', 'customer_id', 'technician_id', 'machine', 'issue', 'comments', 'completed')


class Equipment(db.Model):
    __tablename__ = 'equipment'

    serial_number = db.Column(db.String, primary_key=True)
    make = db.Column(db.String)
    model = db.Column(db.String)
    manufacture_year = db.Column(db.Integer)
    cycle_count = db.Column(db.Integer)
    owner = db.Column(db.String, db.ForeignKey('customer.customer_id'))
    job_equipment = db.relationship(Jobcard, backref='equip_job', lazy=True)


class EquipmentSchema(ma.Schema):
    class Meta:
        fields = ('serial_number', 'make', 'model', 'manufacture_year', 'cycle_count', 'owner')


class Customer(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.String, primary_key=True)
    business_name = db.Column(db.String)
    branch_name = db.Column(db.String)
    contact_name = db.Column(db.String)
    phone_number = db.Column(db.String)
    email_address = db.Column(db.String)
    location = db.Column(db.String)
    job_customer = db.relationship(Jobcard, backref='customer_job', lazy=True)
    equipment_customer = db.relationship(Equipment, backref='customer_equip', lazy=True)


class CustomerSchema(ma.Schema):
    class Meta:
        fields = (
            'customer_id', 'business_name', 'branch_name', 'contact_name', 'phone_number', 'email_address', 'location'
        )


class Staff(db.Model):
    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    role = db.Column(db.String)
    phone_number = db.Column(db.String)
    email_address = db.Column(db.String)
    job_staff = db.relationship(Jobcard, backref='technician', lazy=True)


class StaffSchema(ma.Schema):
    class Meta:
        fields = ('staff_id', 'first_name', 'last_name', 'role', 'phone_number', 'email_address')


class Parts(db.Model):
    __tablename__ = 'parts'

    part_number = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer)
    supplier = db.Column(db.String)
    # Could add in a make and model section as well


class PartsSchema(ma.Schema):
    class Meta:
        fields = ('part_number', 'name', 'quantity', 'supplier')