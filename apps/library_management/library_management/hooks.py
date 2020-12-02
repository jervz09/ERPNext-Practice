# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "library_management"
app_title = "Library Management"
app_publisher = ""
app_description = ""
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = ""
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_management/css/library_management.css"
# app_include_js = "/assets/library_management/js/library_management.js"

# include js, css files in header of web template
web_include_css = "/assets/library_management/css/library_management.css"
web_include_js = "/assets/library_management/js/library_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "library_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "library_management.install.before_install"
# after_install = "library_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"Library Management": {
# 		"get_logged_user": "library_management.custom_api.api_library.get_logged_user",
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    # "all": [
    # 	"library_management.scheduler_task.all"
    # ],
    # "daily": [
    # 	"library_management.scheduler_task.daily"
    # ],
    # "hourly": [
    # 	"library_management.scheduler_task.hourly"
    # ],
    # "weekly": [
    # 	"library_management.scheduler_task.weekly"
    # ],
    # "monthly": [
    # 	"library_management.scheduler_task.monthly"
    # ],
    "cron": {
        "0/10 * * * *": [
            # "library_management.scheduler_task.daily",
            # "library_management.scheduler_task.dailyOne",
            "library_management.task.daily"
        ],
    }
}

# Testing
# -------

# before_tests = "library_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library_management.task.get_dashboard_data"
# }


# website_route_rules = [
#     {"from_route": "/custom_api/get_context", "to_route": "library_management/custom_api/api_library"},
# ]