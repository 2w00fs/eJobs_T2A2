import secrets

from modules.shared import db, cute
from tables.build_jobcards import default_jobcards as jbcrds
from modules.schemas import Jobcard, JobcardSchema, Customer, Equipment, Staff
from modules.html_strings import index_list, update_card


def job_seed():
    entries = []
    for i in jbcrds:
        entries.append(Jobcard(
            job_id=i['job_id'],
            customer_id=i['customer_id'],
            technician_id=i['technician_id'],
            machine=i['machine'],
            issue=i['issue'],
            comments=i['comments'],
            completed=i['completed']
        ))
    return entries


def all_jobs(completed=None):
    """
    :param completed: "true" | "false" [optional]

    by default, selects all jobs in the database and returns them
    """
    print(completed)

    if completed == 'false':
        # filters results based on the status of Completed
        not_completed = cute(db.select(Jobcard).filter(Jobcard.completed == False)).scalars()
        nclist = JobcardSchema(many=True).dump(not_completed)
        return nclist

    if completed == 'true':
        complete = cute(db.select(Jobcard).filter(Jobcard.completed == True)).scalars()
        clist = JobcardSchema(many=True).dump(complete)
        return clist

    j = cute(db.select(Jobcard)).scalars()
    jlist = JobcardSchema(many=True).dump(j)
    return jlist


def get_job_by_id(id):
    # uses a JOIN query to select a customers data when their id is assigned to a job
    job_cust_info = cute(db.select(Customer.business_name, Customer.branch_name, Customer.contact_name,
                                   Customer.location, Jobcard.issue, Jobcard.comments, Jobcard.job_id)
                         .join_from(Customer, Jobcard).filter_by(job_id=id)).first()
    # deconstructs customer and job info returned from query
    bname, branch, cname, location, issue, comments, jid = job_cust_info

    # another JOIN query is made to get details about the equipment that is listed on the job card
    job_equip_info = cute(db.select(Equipment.serial_number, Equipment.make, Equipment.model,
                                    Equipment.manufacture_year, Equipment.cycle_count)
                          .join_from(Equipment, Jobcard).filter_by(job_id=id)).first()
    # deconstructs equipment info returned from query
    sn, make, model, mfy, cc = job_equip_info
    # pass all returned values in to very basic html to be displayed
    return update_card(jid, bname, branch, cname, make, mfy, sn, model, cc, issue)


def update_job(job_id, comments):
    print(comments)
    j = cute(db.select(Jobcard).filter(Jobcard.job_id == job_id)).scalar()
    print(j.issue)
    j.comments = comments
    j.completed = True
    db.session.commit()
    return f'<html style="background-color:black"><h1 style="color:white">Job Card Submitted!</h1> \
            {index_list()}</html>'


def new_card(cust_id, issue, machine, technician):
    tech = cute(db.select(Staff).filter(Staff.staff_id == technician)).scalar()
    cust = cute(db.select(Customer).filter(Customer.customer_id == cust_id)).scalar()
    equip = cute(db.select(Customer).filter(Equipment.serial_number == machine)).scalar()

    new_job = Jobcard(job_id=secrets.token_hex(3), issue=issue)

    tech.job_staff.extend([new_job])
    cust.job_customer.extend([new_job])
    equip.job_equipment.extend([new_job])
    db.session.commit()
    return f'<html style="background-color:black"><h1 style="color:white">Job Created</h1> \
            {index_list()}</html>'
