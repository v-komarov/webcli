#coding:utf-8

import urllib2
from db import getrandomip, getfreerandomip
from conf import radtest_host, radtest_port


def checkrad(mac,ip):
    """Testing radius server"""
    url = "http://{}:{}/{}/{}".format(radtest_host,radtest_port,mac,ip)
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        result = response.read()
        return result
    except:
        return 'Error'


def checkdata(mac):
    """Data of checking radius"""
    result = []
    ip1 = getfreerandomip()
    result.append({'mac':mac,'ip':ip1,'result':checkrad(mac,ip1)})
    ip2 = getrandomip()
    result.append({'mac':mac,'ip':ip2,'result':checkrad(mac,ip2)})
    return result
