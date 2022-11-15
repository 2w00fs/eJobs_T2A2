import secrets

from tables.build_equipment import default_equipment as eqpmnt
from modules.shared import db, cute
from modules.schemas import Equipment, EquipmentSchema, Customer
from modules.html_strings import index_list


def equipment_seed():
    entries = []
    for i in eqpmnt:
        entries.append(Equipment(
            serial_number=i['serial_number'],
            make=i['make'],
            model=i['model'],
            manufacture_year=i['manufacture_year'],
            cycle_count=i['cycle_count'],
            owner=i['owner']
        ))

    return entries


def all_equipment():
    # SELECTS all equipment in the database and returns it
    c = cute(db.select(Equipment)).scalars()
    clist = EquipmentSchema(many=True).dump(c)
    return clist


def get_equip_by_sn(sn):
    # returns equipment data based on the serial number
    c = cute(db.select(Equipment).filter(Equipment.serial_number == sn)).scalars()
    clist = EquipmentSchema(many=True).dump(c)
    print(clist)
    return clist


def get_equip_by_cust_id(id):
    # uses a JOIN query to select a machines data when its sn is assigned to a customer
    eq_cust_info = cute(db.select(Equipment)
                         .join_from(Customer, Equipment).filter_by(customer_id=id)).scalars()
    # deconstructs customer and job info returned from query
    eq_list = EquipmentSchema(many=True).dump(eq_cust_info)
    return eq_list


def new_equipment(cust_id, make, model, cycle_count, manufactured, sn=secrets.token_hex(4)):
    # searches for the customer id, verifying that it exists
    cust = cute(db.select(Customer).filter(Customer.customer_id == cust_id)).scalar()
    # adds new entry for the equipment
    new = Equipment(serial_number=sn, make=make, model=model, manufacture_year=manufactured, cycle_count=cycle_count)
    # binds the customer id to the machine
    cust.equipment_customer.extend([new])
    db.session.commit()
    return f'<html style="background-color:black"><h1 style="color:white">Equipment Added</h1> \
    {index_list()}</html>'
