from flask import Flask,request,session,redirect,url_for,render_template,g

from util import MessageUtil
from config import *

import actions.GenericAction as GA

app = Flask(__name__, "/static")
app.config.from_pyfile('config.py')

## TODO: modularize
ROUTES = {
    "/":{
        "name":"main",
        "controller":GA.main,
        "methods":['get','post'],
    },
}

@app.context_processor
def injectMessages():
    ret = {}
    errors = MessageUtil.getErrors()
    if errors != None:
        ret["errors"] = errors
    msgs = MessageUtil.getMessages()
    if msgs != None:
        ret["messages"] = msgs
    return ret

@app.context_processor
def session_info():
    try:
        if g.has_key("logged_in"):
            return {"logged_in": g.logged_in}
    except Exception,e:
        print "Exception checking login state: %s" % (e.message,)
    return {"logged_in": False}

@app.context_processor
def form_passthrough():
    vals = {}
    [vals.update({k:request.args[k]}) for k in request.args.keys()]
    [vals.update({k:request.form[k]}) for k in request.form.keys()]
    return {"form_vals":vals}

def app_setup():
    init_model()
    for path in ROUTES.keys():
        if ROUTES[path].has_key("methods"):
            methods = ROUTES[path]["methods"]
        else: methods=["GET"]
        app.add_url_rule(path, ROUTES[path]["name"], ROUTES[path]["controller"], methods=methods)
    app.debug = DEBUG

def run(port=PORT):
    app_setup()
    app.run(port=port, use_evalex=False, use_reloader=False)

if __name__ == "__main__":
    run(port=PORT)
else:
    app_setup()

