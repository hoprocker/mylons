from flask import render_template,flash,get_flashed_messages,request,redirect,url_for,Module,make_response
"""
TODO : three necessary variables:

MODULE : a Module instance
PATH : the part after '/admin/', the base path
ROUTES : route->name,controller[,method] mappings
"""

GENERIC_TEMPLATE = "generic.html"
def main(**kwargs):
    return render_template(GENERIC_TEMPLATE)

"""
TODO : 

routes defined after endpoints

example:

ROUTES = {
    "/":{
        "name":"main",
        "controller":main,
    },
}
"""
