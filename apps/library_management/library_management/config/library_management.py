
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
            "label": _("Library Management"),
            "items": [
                {
					"type": "doctype",
					"name": "Article",
					"description":_("Article."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Library Member",
					"description":_("Library Member."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Library Membership",
					"description":_("Library Membership."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Library Settings",
					"description":_("Library Settings."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Library Transaction",
					"description":_("Library Transaction."),
					"onboard": 1,
				},
            ]
        }
	]