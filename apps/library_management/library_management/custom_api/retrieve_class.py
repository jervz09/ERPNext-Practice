from __future__ import unicode_literals
import frappe

class article_doc:
    def __init__(self):
        pass
    
    def retrieveData(self,_name):
        data = frappe.db.get_list('Article', 
                filters={
                    'article_name': _name or ""]
                },
                fields = ['article_name', 'author', 'description', 'creation'])
        return {
            "data" : data
        }
