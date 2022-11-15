import datetime


def make_new_card(jid, bname, branch, cname, make, mfy, sn, model, cc, issue):
    html = '<html><body style="text-align:center"><h1>JOB CARD</h1><br><br>' \
        + f'<h3>Job Number #{jid}<h2>BENCH TOP STERILISER CARD</h2><br><br><br>' \
        + '<form action="/jobs/new/" method="post"'
    # business details
    biz = '<label for="business_name">Business:  </label>' \
        + f'<input type="text" id="business_name" name="business_name" value="{bname}"><br><br><br>'
    branch = '<label for="branch_name">Branch:  </label>' \
        + f'<input type="text" id="branch_name" name="branch_name" value="{branch}"><br><br><br>'
    contact = '<label for="contact_name">Contact:  </label>' \
        + f'<input type="text" id="contact_name" name="contact_name" value="{cname}"><br><br><br>' \
        + f'<input type="text" style="visibility:hidden;" id="jid" name="jid" value="{jid}"><br>' \
        # machine details
    make = '<label for="make">Make: </label>' \
        + f'<input type="text" id="make" name="make" value="{make}">'
    yom = '<label for="yom">  Year of Manufacture:  </label>' \
        + f'<input type="text" id="yom" name="yom" value="{mfy}">'
    sn = '<label for="sn">  S/N:  </label>' \
        + f'<input type="text" id="sn" name="sn" value="{sn}"><br><br><br>'
    model = '<label for="model">Model:  </label>' \
        + f'<input type="text" id="model" name="model" value="{model}">'
    cycles = '<label for="cycles">  Cycles:  </label>' \
        + f'<input type="text" id="cycles" name="cycles" value="{cc}">'
    x = datetime.datetime.now()
    date = '<label for="date">  Date:  </label>' \
        + f'<input type="text" id="date" name="date" value="{(x.strftime("%d/%m/%y"))}"><br><br>'
    issue = '<label for="model">Issue</label><br>' \
        + f'<h4>{issue}</h4>'
    comments = '<label for="cycles">Comments:  </label><br><br>' \
        + '<input style="width:50vw; height:15vh;" type="text" id="comments" name="comments" value=""' \
        + 'placeholder="Enter your comments here"><br><br><br>'
    end = '<input type="submit" value="Submit">' \
        + '</form>' \
        + '</body></html>'
    all = html + biz + branch + contact + make + yom + sn + model + cycles + date + issue + comments + end
    return all


def update_card(jid, bname, branch, cname, make, mfy, sn, model, cc, issue):
    html = '<html><body style="text-align:center"><h1>JOB CARD</h1><br><br>' \
        + f'<h3>Job Number #{jid}<h2>BENCH TOP STERILISER CARD</h2><br><br><br>' \
        + '<form action="/jobs/update/" method="post"'
    # business details
    biz = '<label for="business_name">Business:  </label>' \
        + f'<input type="text" id="business_name" name="business_name" value="{bname}"><br><br><br>'
    branch = '<label for="branch_name">Branch:  </label>' \
        + f'<input type="text" id="branch_name" name="branch_name" value="{branch}"><br><br><br>'
    contact = '<label for="contact_name">Contact:  </label>' \
        + f'<input type="text" id="contact_name" name="contact_name" value="{cname}"><br><br><br>' \
        + f'<input type="text" style="visibility:hidden;" id="job_id" name="job_id" value="{jid}"><br>' \
        # machine details
    make = '<label for="make">Make: </label>' \
        + f'<input type="text" id="make" name="make" value="{make}">'
    yom = '<label for="yom">  Year of Manufacture:  </label>' \
        + f'<input type="text" id="yom" name="yom" value="{mfy}">'
    sn = '<label for="sn">  S/N:  </label>' \
        + f'<input type="text" id="sn" name="sn" value="{sn}"><br><br><br>'
    model = '<label for="model">Model:  </label>' \
        + f'<input type="text" id="model" name="model" value="{model}">'
    cycles = '<label for="cycles">  Cycles:  </label>' \
        + f'<input type="text" id="cycles" name="cycles" value="{cc}">'
    x = datetime.datetime.now()
    date = '<label for="date">  Date:  </label>' \
        + f'<input type="text" id="date" name="date" value="{(x.strftime("%d/%m/%y"))}"><br><br>'
    issue = '<label for="comments">Issue</label><br>' \
        + f'<h4>{issue}</h4>'
    comments = '<label for="comments">Comments:  </label><br><br>' \
        + '<input style="width:50vw; height:15vh;" type="text" id="comments" name="comments" value=""' \
        + 'placeholder="Enter your comments here"><br><br><br>'
    end = '<input type="submit" value="Submit">' \
        + '</form>' \
        + '</body></html>'
    all = html + biz + branch + contact + make + yom + sn + model + cycles + date + issue + comments + end
    return all


def cust_template():
    html = '<html><body><h1>Add New Customer</h1><h2>Business</h2>' \
           + '<form action="/customer/new" method="post"'
    biz = '<label for="business_name">Business Name:  </label>' \
          + '<input type="text" id="business_name" name="business_name" value=""><br><br>'
    branch = '<label for="branch_name">Branch Name:  </label>' \
             + '<input type="text" id="branch_name" name="branch_name" value=""><br><br>'
    contact = '<label for="contact_name">Contact Name:  </label>' \
              + '<input type="text" id="contact_name" name="contact_name" value=""><br><br>'
    phone = '<label for="phone_number">Phone Number:  </label>' \
            + '<input type="text" id="phone_number" name="phone_number" value=""><br><br>'
    email = '<label for="email_address">Email Address:  </label>' \
            + '<input type="text" id="email_address" name="email_address" value=""><br><br>'
    location = '<label for="location">Location:  </label>' \
               + '<input type="text" id="location" name="location" value=""><br><br>'
    end = '<input type="submit" value="Submit">' \
          + '</form>' \
          + '</body></html>'
    all = html + biz + branch + contact + phone + email + location + end
    return all


def parts_template():
    html = '<html><body><h1>Add New Part</h1>' \
           + '<form action="/parts/post_part" method="post"'
    pn = '<label for="part_number">Part Number:  </label>' \
          + '<input type="text" id="part_number" name="part_number" value=""><br><br>'
    name = '<label for="name">Name:  </label>' \
             + '<input type="text" id="name" name="name" value=""><br><br>'
    quantity = '<label for="quantity">Quantity:  </label>' \
              + '<input type="text" id="quantity" name="quantity" value=""><br><br>'
    supplier = '<label for="supplier">Supplier:  </label>' \
            + '<input type="text" id="supplier" name="supplier" value=""><br><br>'
    end = '<input type="submit" value="Submit">' \
          + '</form>' \
          + '</body></html>'
    all = html + pn + name + quantity + supplier + end
    return all


def index_list():
    html = '<div id="index" style="background-color:black;color:white;">' \
           + '<a href="/create_all/"><h1>create_all/</h1></a>' \
           + '<a href="/staff/all/"><h1>/staff/all/</h1></a>' \
           + '<a href="/staff/id/"><h1>/staff/id/:id:</h1></a>' \
           + '<a href="/staff/delete/"><h1>/staff/delete/:id:/</h1></a>' \
           + '<a href="/equipment/all/"><h1>equipment/all/</h1></a>' \
           + '<a href="/equipment/sn/"><h1>equipment/sn/:sn:/</h1></a>' \
           + '<a href="/equipment/customer/"><h1>equipment/customer/:id:/</h1></a>' \
           + '<a href="/customers/all/"><h1>customers/all/</h1></a>' \
           + '<a href="/customers/id/"><h1>customers/id/:id:/</h1></a>' \
           + '<a href="/customer/add_form"><h1>customer/add_form/</h1></a>' \
           + '<a href="/jobs/all/"><h1>jobs/all/</h1></a>' \
           + '<a href="/jobs/id/"><h1>jobs/id/:id:/</h1></a>' \
           + '<a href="/jobs/add_form/"><h1>jobs/add_form/</h1></a>' \
           + '<a href="/parts/all/"><h1>parts/all/</h1></a>' \
           + '<a href="/parts/number/"><h1>parts/number/:pn:/</h1></a>' \
           + '<a href="/parts/new/"><h1>parts/new/</h1></a>' \
           + '</div>'
    return html
