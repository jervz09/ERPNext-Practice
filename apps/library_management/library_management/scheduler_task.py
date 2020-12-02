from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, nowdate, formatdate, add_days
import logging
import csv


logging.basicConfig(level=logging.INFO)


def dailyOne():
    # frappe.throw("background Job!")
    # stuff to do every 1 minute
    error_messages = "Hello World 1 minute Log"
    # logging.info(get_overdue(5))
    frappe.log_error(get_overdue(5), "WooCommerce Error")


def daily():
    loan_period = frappe.db.get_value("Library Management Settings",
                                      None, "loan_period")

    overdue = get_overdue(loan_period)

    frappe.log_error(overdue, "New Logging")
    frappe.log_error(overdue.items(), "Second Logging")

    for member, items in overdue.items():
        content = """<h2>Following Items are Overdue</h2>
    	<p>Please return them as soon as possible</p><ol>"""

        frappe.log_error(member, "Third Logging")
        frappe.log_error(items, "Third Logging")


        for i in items:
            content += "<li>{0} ({1}) due on {2}</li>".format(i.name,
                                                              i.article,
                                                              formatdate(add_days(i.transaction_date, loan_period)))

        content += "</ol>"

    # recipient = frappe.db.get_value("Library Member", member, "email_id")
    # frappe.sendmail(recipients=[recipient],
    # 	sender="test@example.com",
    # 	subject="Library Articles Overdue", content=content, bulk=True)


def get_overdue(loan_period):
    # check for overdue articles
    today = nowdate()

    overdue_by_member = {}
    articles_transacted = []

    for d in frappe.db.sql("""select *,date as transaction_date
        from `tabLibrary Transaction`
        order by transaction_date desc, modified desc""", as_dict=True):

        if d.article in articles_transacted:
            continue

        if d.transaction_type == "Issue" and \
                date_diff(today, d.transaction_date) > loan_period:
            overdue_by_member.setdefault(d.library_member, [])
            overdue_by_member[d.library_member].append(d)

        articles_transacted.append(d.article)

    return d
    # def order(*args, **kwargs):
    # try:
    # 	_order(*args, **kwargs)
    # except Exception:
    # 	error_message = frappe.get_traceback()+"\n\n Request Data: \n"+json.loads(frappe.request.data).__str__()
    # 	frappe.log_error(error_message, "WooCommerce Error")
    # 	raise
