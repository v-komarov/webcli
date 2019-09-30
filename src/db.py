#coding:utf-8

import datetime
import MySQLdb
from conf import mysql_host, mysql_user, mysql_passwd, mysql_db


conn = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)


def get_canals_free():
    """List of free canals"""
    cur = conn.cursor()
    cur.execute("SELECT ip FROM radfreecharge ORDER BY ip")
    data = cur.fetchall()
    return data



def get_canals():
    """List of canals"""
    cur = conn.cursor()
    cur.execute("SELECT value FROM radpackets WHERE pid=0 ORDER BY value")
    data = cur.fetchall()
    return data



def wlog(user, note):
    """Writing user action"""
    now = datetime.datetime.now()
    cur = conn.cursor()
    cur.execute("""INSERT user_logs(date_time,username,action) VALUES(%s,%s,%s);""", (now,user,note))
    conn.commit()
    return 'Ok'


def getlog():
    """Getting log data"""
    cur = conn.cursor()
    cur.execute("SELECT date_time,username,action FROM user_logs ORDER BY date_time DESC LIMIT 200")
    data = cur.fetchall()
    return data



def getfreeradomip():
    """Getting random ip free canal"""
    cur = conn.cursor()
    cur.execute("SELECT ip FROM radfreecharge ORDER BY RAND() LIMIT 1")
    data = cur.fetchone()[0]
    return data


def getradomip():
    """Getting random ip canal"""
    cur = conn.cursor()
    cur.execute("SELECT value FROM radpackets WHERE pid=0  ORDER BY RAND() LIMIT 1")
    data = cur.fetchone()[0]
    return data

