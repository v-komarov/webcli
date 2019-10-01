#coding:utf-8

import datetime
import ipaddress
import MySQLdb
from conf import mysql_host, mysql_user, mysql_passwd, mysql_db


conn = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)


def get_canals_free():
    """List of free canals"""
    cur = conn.cursor()
    cur.execute("SELECT ip FROM radfreecharge ORDER BY ip")
    data = cur.fetchall()
    cur.close()
    return data



def get_canals():
    """List of canals"""
    cur = conn.cursor()
    cur.execute("SELECT value FROM radpackets WHERE pid=0 ORDER BY value")
    data = cur.fetchall()
    cur.close()
    return data



def wlog(user, note):
    """Writing user action"""
    now = datetime.datetime.now()
    cur = conn.cursor()
    cur.execute("""INSERT user_logs(date_time,username,action) VALUES(%s,%s,%s);""", (now,user,note))
    conn.commit()
    cur.close()
    return 'Ok'


def getlog():
    """Getting log data"""
    cur = conn.cursor()
    cur.execute("SELECT date_time,username,action FROM user_logs ORDER BY date_time DESC LIMIT 200")
    data = cur.fetchall()
    cur.close()
    return data



def getfreerandomip():
    """Getting random ip free canal"""
    cur = conn.cursor()
    cur.execute("SELECT ip FROM radfreecharge ORDER BY RAND() LIMIT 1")
    data = cur.fetchone()[0]
    cur.close()
    return data


def getrandomip():
    """Getting random ip canal"""
    cur = conn.cursor()
    cur.execute("SELECT value FROM radpackets WHERE pid=0  ORDER BY RAND() LIMIT 1")
    data = cur.fetchone()[0]
    cur.close()
    return data.split()[0]


def getmacs():
    """Getting temperrary macs"""
    cur = conn.cursor()
    cur.execute("SELECT date_time,mac FROM macs_tmp ORDER BY date_time DESC")
    data = cur.fetchall()
    cur.close()
    return data



def addfreecanal(canal, username):
    """Adding free canal"""
    cur = conn.cursor()
    ips = canal.split("-")
    if len(ips) == 1: 
        cur.execute("CALL writefreecanal(%s)", (ips[0],))
        conn.commit()

    if len(ips) == 2:
        ip = ipaddress.ip_address(ips[0].decode("utf-8"))
        ip_end = ipaddress.ip_address(ips[1].decode("utf-8"))

        while ip <= ip_end:

            cur.execute("CALL writefreecanal(%s)", (str(ip),))
            conn.commit()
            ip += 1
     
    wlog(username, "Добавление ip адресов общедоступных каналов: {}".format(canal))

    cur.close()
    return 'Ok'




def delfreecanal(canal, username):
    """Deleting free canal"""
    cur = conn.cursor()
    ips = canal.split("-")
    if len(ips) == 1: 
        cur.execute("DELETE FROM radfreecharge WHERE ip=%s", (ips[0],))
        conn.commit()

    if len(ips) == 2:
        ip = ipaddress.ip_address(ips[0].decode("utf-8"))
        ip_end = ipaddress.ip_address(ips[1].decode("utf-8"))

        while ip <= ip_end:

            cur.execute("DELETE FROM radfreecharge WHERE ip=%s", (str(ip),))
            conn.commit()
            ip += 1
     
    wlog(username, "Удаление ip адресов общедоступных каналов: {}".format(canal))

    cur.close()
    return 'Ok'




def addcanal(canal, username):
    """Adding canal"""
    cur = conn.cursor()
    ips = canal.split("-")
    if len(ips) == 1: 
        cur.execute("CALL writecanal(%s)", (ips[0],))
        conn.commit()

    if len(ips) == 2:
        ip = ipaddress.ip_address(ips[0].decode("utf-8"))
        ip_end = ipaddress.ip_address(ips[1].decode("utf-8"))

        while ip <= ip_end:

            cur.execute("CALL writecanal(%s)", (str(ip),))
            conn.commit()
            ip += 1
     
    wlog(username, "Добавление ip адресов коммерческих каналов: {}".format(canal))

    cur.close()
    return 'Ok'




def delcanal(canal, username):
    """Deleting canal"""
    cur = conn.cursor()
    ips = canal.split("-")
    if len(ips) == 1: 
        cur.execute("DELETE FROM radpackets WHERE value=%s AND pid=0", (ips[0],))
        conn.commit()

    if len(ips) == 2:
        ip = ipaddress.ip_address(ips[0].decode("utf-8"))
        ip_end = ipaddress.ip_address(ips[1].decode("utf-8"))

        while ip <= ip_end:

            cur.execute("DELETE FROM radpackets WHERE value=%s AND pid=0", (str(ip),))
            conn.commit()
            ip += 1
     
    wlog(username, "Удаление ip адресов коммерческих каналов: {}".format(canal))

    cur.close()
    return 'Ok'



def wmac(mac,username):
    """Writing temperrary macs"""
    cur = conn.cursor()
    cur.execute("CALL writemac(%s,%s)", (mac,datetime.datetime.now()))

    wlog(username, "Добавлен временный MAC адрес: {}".format(mac))

    cur.close()
    return 'Ok'
