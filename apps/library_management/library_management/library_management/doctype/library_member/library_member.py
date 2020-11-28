# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jhay Ar Ariola and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class LibraryMember(Document):
    # this method will run every time a document is saved
    def before_save(self):
        self.full_name = "{} {}".format(self.first_name,self.last_name)