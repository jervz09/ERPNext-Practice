# Copyright (c) 2013, Frappe
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, nowdate, formatdate, add_days
import csv


def daily():
    loan_period = frappe.db.get_value("Library Management Settings",
                                      None, "loan_period")

    overdue = get_overdue(loan_period)

    logDict = {}

    # for member, items in overdue.items():

    #     if member == "name" or member == "transaction_date":
    #         logDict[member] = items
    with open('overdue.csv', mode='w') as csv_file:
        fieldnames = [ 'name','docstatus', 'library_member', 'type', 'transaction_date', 'article']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for x in overdue:
            writer.writerow(x)
            
            frappe.log_error(x, "New Logging")


def get_overdue(loan_period):
    # check for overdue articles
    today = nowdate()

    overdue_by_member = {}
    articles_transacted = []
    helloworld = {}
    y = frappe.db.sql("""select name,article, library_member, type, date as transaction_date, docstatus
        from `tabLibrary Transaction`
        order by transaction_date desc""", as_dict=True)

    d = frappe.db.get_list('Library Transaction',
                           fields=['name', 'article', 'library_member', 'type', 'date'],
                           order_by='date desc',
                           as_list=True
                           )

    # if d.article in articles_transacted:
    #     continue

    # if d.transaction_type == "Issue" and \
    #         date_diff(today, d.transaction_date) > loan_period:
    #     overdue_by_member.setdefault(d.library_member, [])
    #     overdue_by_member[d.library_member].append(d)

    # articles_transacted.append(d.article)
    
    return y
