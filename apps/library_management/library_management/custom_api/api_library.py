from __future__ import unicode_literals
import frappe
# from retrieve_class import article_doc 

fields = ['article_name', 'author', 'description', 'creation']

"""
@api {get} /api/method/library_management.custom_api.api_library.get_article:search Request Article information
@apiName get_article
@apiGroup Article

@apiParam {String} search for Article Name.

@apiSuccess {String} article_name  Article Name of the Article List.
@apiSuccess {String} author  Author Name of the Article.
@apiSuccess {String} description Description of the Article.
"""

@frappe.whitelist()
def get_article(*args,**kwargs):

    res = ""
    getInfo = kwargs.get
    search = getInfo("search")

    res = frappe.db.get_list('Article', 
                filters={
                    'article_name': ['like', '%{}%'.format(search or "")]
                },
                fields = fields,
                order_by="{} {}".format(getInfo("order_by") or "creation",getInfo("sort") or "desc"),
                start=getInfo("page") or 0,
                limit_page_length=getInfo("size") or 20)

    count = frappe.db.count('Article')

    return {
        "data": res,
        "count": "{} total rows".format(count),
        "msg": "Successfully retrieved data."
    }

@frappe.whitelist()
def post_article(*args,**kwargs):
    
    kwargs = frappe._dict(kwargs)
    kwargs.pop("cmd")
    kwargs["doctype"] = "Article"
    try:
        todo = frappe.get_doc(kwargs)
        todo.insert()
        msg = "Record Inserted Successfully"
    except Exception as e:
        msg = str(e).replace("\\",'')
    return {
        "data": todo,
        "msg": msg
    }

@frappe.whitelist()
def put_article(*args,**kwargs):
    
    kwargs = frappe._dict(kwargs)
    name = kwargs.get("name")
    kwargs.pop("name")
    kwargs.pop("cmd")

    _data = exist_article(name)
    try:
        if _data:
            msg = "Totoo"
            data = frappe.db.set_value('Article', name, kwargs)
    except:
        msg = "Mali"

    return {
        "data": _data,
        "msg": msg
    }

@frappe.whitelist()
def exist_article(name=""):
    if_exists = frappe.db.exists('Article', name)
    return if_exists


@frappe.whitelist()
def retrieveData(*args,**kwargs):
    data = frappe.db.get_list('Article', 
            filters={
                'article_name': "test-1" or ""
            },
            fields = ['article_name', 'author', 'description', 'creation'])
    return {
        "data" : data
    }