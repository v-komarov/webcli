#coding:utf-8

import bottle
from bottle import route, run, get, post, request, template, static_file, redirect
from auth import auth as login
from db import get_canals_free, get_canals, getlog, getmacs
from beaker.middleware import SessionMiddleware



session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}


app = SessionMiddleware(bottle.app(), session_opts)




def chsess():
    session = bottle.request.environ['beaker.session']
    if session.get('username', False):
        return True
    else:
        return False



def getuser():
    """Getting username"""
    session = bottle.request.environ['beaker.session']
    return session.get('username', 'Error')



@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static/')



@get("/")
def authform():
    if chsess():
        return template('tpls/radtest.tpl')
    else:
        redirect("/auth")



@get("/auth")
def auth():
    return template("tpls/auth.tpl")



@post("/auth")
def authuser():
    username = request.forms.get("username")
    password = request.forms.get("password")
    if login(username,password):
        session = bottle.request.environ['beaker.session']
        session["username"] = username
        return template('tpls/radtest.tpl')
    else:
        return template('tpls/auth.tpl')  



@post("/radtest")
def radtest():
    if chsess():
        return template('tpls/radtest.tpl')
    else:
        return template('tpls/auth.tpl')



@get("/radtest")
def radtest():

    return template('tpls/radtest.tpl')




@get("/canalfree")
def canalfree():
    if chsess():
        return template('tpls/canals_free.tpl', canals=get_canals_free())
    else:
        redirect("/auth")



@get("/canal")
def canalfree():
    if chsess():
        return template('tpls/canals.tpl', canals=get_canals())
    else:
        redirect("/auth")




@get("/macs")
def macs():
    if chsess():
        return template('tpls/set_mac.tpl', macs=getmacs())
    else:
        redirect("/auth")



@get("/log")
def macs():
    if chsess():
        return template('tpls/logs.tpl', data=getlog())
    else:
        redirect("/auth")





@get("/exit")
def exit():
    """quit"""
    session = bottle.request.environ['beaker.session']
    del session["username"]
    redirect("/")



if __name__ == "__main__":
    run(app=app, host="", port=8000)
    
    
#app = bottle.default_app()


