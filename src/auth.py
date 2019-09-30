#coding:utf-8


import urllib2
import json
import bottle
from bottle import request, response, redirect
from conf import auth_service



def auth(username,password):
    """Registration of user"""
    url = "http://{}?action=user-kis&login={}&passwd={}".format(auth_service,username,password)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    d = json.loads(response.read())
    if d['result'] == u'ok':
        return True
    else:
        return False 



def chlogin(session):
    def wrapper(fn):
        """checking user's session"""
        def ch(*args, **kwargs):
            if session.get("username",None):
                redirect("/")
            else:
                return fn
    return wrapper
