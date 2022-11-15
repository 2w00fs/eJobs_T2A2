import secrets

from tables.build_customer import default_customers as cstmr
from modules.shared import db, cute
from modules.schemas import Customer, CustomerSchema
from modules.html_strings import index_list


def customer_seed():
    entries = []
    for i in cstmr:
        entries.append(Customer(
            customer_id=i['customer_id'],
            business_name=i['business_name'],
            branch_name=i['branch_name'],
            email_address=i['contact_name'],
            phone_number=i['phone_number'],
            contact_name=i['email_address'],
            location=i['location']
        ))
    return entries


def all_customers():
    c = cute(db.select(Customer)).scalars()
    clist = CustomerSchema(many=True).dump(c)
    return clist


def get_cust_by_id(id):
    c = cute(db.select(Customer).filter(Customer.customer_id == id)).scalars()
    clist = CustomerSchema(many=True).dump(c)
    print(clist)
    return clist


def add_customer(business_name, branch_name, contact_name, phone_number, email_address, location):
    v = Customer(
        customer_id=secrets.token_hex(3),
        business_name=business_name,
        branch_name=branch_name,
        contact_name=contact_name,
        phone_number=phone_number,
        email_address=email_address,
        location=location
    )
    db.session.add(v)
    db.session.commit()
    return f'<html style="background-color:black"><h1 style="color:white">Customer Created!</h1> \
    {index_list()}</html>'
