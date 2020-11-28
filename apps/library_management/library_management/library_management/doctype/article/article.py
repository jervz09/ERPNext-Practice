# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jhay Ar Ariola and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class Article(WebsiteGenerator):
	website = frappe._dict(
		condition_field = "show_in_website",
		template = "templates/article.html",
		page_title_field = "article_name",
		no_cache = 1
	)