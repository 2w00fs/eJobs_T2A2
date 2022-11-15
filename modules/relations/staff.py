import secrets

from tables.build_staff import default_staff as stff
from modules.shared import db, cute
from modules.schemas import Staff, StaffSchema
from modules.html_strings import index_list


def staff_seed():
    entries = []
    for i in stff:
        entries.append(Staff(
            staff_id=i['staff_id'],
            first_name=i['first_name'],
            last_name=i['last_name'],
            role=i['role'],
            phone_number=i['phone_number'],
            email_address=i['email_address']
        ))
    return entries


def new_staff(first_name, last_name, role, phone_number, email_address):
    new = Staff(secrets.token_hex(5), first_name, last_name, role, phone_number, email_address)
    db.session.add(new)
    db.session.commit()
    return f'<html style="background-color:black"><body style="color:white"><h1>New Staff Member Added!</h1> \
            {index_list()} </body></html>'


def all_staff():
    # SELECTS all staff in the database and returns them
    c = cute(db.select(Staff)).scalars()
    clist = StaffSchema(many=True).dump(c)
    return clist


def get_staff_by_id(id):
    # returns staff data based on their id
    c = cute(db.select(Staff).filter(Staff.staff_id == id)).scalars()
    clist = StaffSchema(many=True).dump(c)
    print(clist)
    return clist


def delete_staff_by_id(id):
    # deletes staff member using their id
    cute(db.select(Staff).filter(Staff.staff_id == id)).delete()
    return f'<html style="background-color:black;color:white"><h1>Staff Member Deleted!</h1> \
           {index_list()} </html>'
