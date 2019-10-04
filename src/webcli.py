#coding:utf-8

import bottle
from bottle import route, run, get, post, request, template, static_file, redirect
from auth import auth as login
from db import get_canals_free, get_canals, getlog, getmacs, addfreecanal, delfreecanal, addcanal, delcanal, wmac
from radtest import checkdata
from beaker.middleware import SessionMiddleware
from conf import radius_name



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


def getusername():
    session = bottle.request.environ['beaker.session']
    return session.get('username', None)




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
        return template('tpls/radtest.tpl', data = [], radius=radius_name)
    else:
        redirect("/auth")



@get("/auth")
def auth():
    return template("tpls/auth.tpl", radius=radius_name)



@post("/auth")
def authuser():
    username = request.forms.get("username")
    password = request.forms.get("password")
    if login(username,password):
        session = bottle.request.environ['beaker.session']
        session["username"] = username
        return template('tpls/radtest.tpl', data = [], radius=radius_name)
    else:
        return template('tpls/auth.tpl', radius=radius_name)  



@post("/radtest")
def radtest2():
    if chsess():
        mac = request.forms.get("mac")
        mac = mac.replace(" ","").replace(":","").replace("-","").replace(".","").upper()
        if mac == "":
            return template('tpls/radtest.tpl', data = [], radius=radius_name)
        else:
            return template('tpls/radtest.tpl', data = checkdata(mac), radius=radius_name)
    else:
        redirect("/auth")



@get("/radtest")
def radtest():

    return template('tpls/radtest.tpl', data = [], radius=radius_name)




@get("/canalfree")
def canalfree():
    if chsess():
        return template('tpls/canals_free.tpl', canals=get_canals_free(), radius=radius_name)
    else:
        redirect("/auth")



@post("/canalfree")
def canalfree2():
    if chsess():
        ip = request.forms.get("ip")
        ip = ip.replace(" ","")
        if len(ip) > 6:
            addfreecanal(ip,getusername())
        redirect("/canalfree")
    else:
        redirect("/auth")




@post("/canalfreedel")
def canalfreedel():
    if chsess():
        ip = request.forms.get("ip")
        ip = ip.replace(" ","")
        if len(ip) > 6:
            delfreecanal(ip,getusername())
        redirect("/canalfree")
    else:
        redirect("/auth")





@get("/canal")
def canal():
    if chsess():
        return template('tpls/canals.tpl', canals=get_canals(), radius=radius_name)
    else:
        redirect("/auth")



@post("/canal")
def canal2():
    if chsess():
        ip = request.forms.get("ip")
        ip = ip.replace(" ","")
        if len(ip) > 6:
            addcanal(ip,getusername())
        redirect("/canal")
    else:
        redirect("/auth")



@post("/canaldel")
def canaldel():
    if chsess():
        ip = request.forms.get("ip")
        ip = ip.replace(" ","")
        if len(ip) > 6:
            delcanal(ip,getusername())
        redirect("/canal")
    else:
        redirect("/auth")






@get("/macs")
def macs():
    if chsess():
        return template('tpls/set_mac.tpl', macs=getmacs(), radius=radius_name)
    else:
        redirect("/auth")



@post("/macs")
def macs2():
    if chsess():
        mac = request.forms.get("mac")
        mac = mac.replace(" ","").replace(".","").replace(":","").replace("-","").upper()
        if len(mac) == 12:
            wmac(mac,getusername())
        redirect("/macs")
    else:
        redirect("/auth")




@get("/log")
def log():
    if chsess():
        return template('tpls/logs.tpl', data=getlog(), radius=radius_name)
    else:
        redirect("/auth")





@get("/exit")
def exit():
    """quit"""
    session = bottle.request.environ['beaker.session']
    del session["username"]
    redirect("/")



if __name__ == "__main__":
    run(app=app, host="0.0.0.0", port=5050)



