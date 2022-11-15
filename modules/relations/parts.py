from tables.build_parts import default_parts as prts
from modules.shared import db, cute
import secrets
from modules.html_strings import index_list
from modules.schemas import Parts, PartsSchema


def parts_seed():
    entries = []
    for i in prts:
        entries.append(Parts(
            part_number=i['part_number'],
            name=i['name'],
            quantity=i['quantity'],
            supplier=i['supplier']
        ))
    return entries


def all_parts():
    # SELECTS all parts in the database and returns them
    c = cute(db.select(Parts)).scalars()
    print(c)
    clist = PartsSchema(many=True).dump(c)
    return clist


def get_parts_by_pn(pn):
    # returns parts data based on the serial number
    c = cute(db.select(Parts).filter(Parts.part_number == pn)).scalars()
    clist = PartsSchema(many=True).dump(c)
    return clist


def new_parts(name, quantity, supplier, part_number=secrets.token_hex(4)):
    new = Parts(
        part_number=part_number,
        name=name,
        quantity=quantity,
        supplier=supplier,
        )
    db.session.add(new)
    db.session.commit()
    return f'<html style="background-color:black;color:white;"><h1>Parts Added!</h1> \
            {index_list()}</html>'


""" IS NOT ACTUALLY IMPLEMENTED
@app.route('/parts/job/<id>/')
def get_parts_by_job_id(id):
    # uses a JOIN query to return parts used on a job
    parts_job_info = cute(db.select(Parts.part_number, Parts.name, Jobcard.quantity)
                         .join_from(Parts, Jobcard).filter_by(job_id=id)).scalars()
    return parts_job_info
"""