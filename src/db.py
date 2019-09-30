#coding:utf-8

import MySQLdb
from conf import mysql_host, mysql_user, mysql_passwd, mysql_db


conn = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)


def get_canals_free():
    cur = conn.cursor()
    cur.execute("SELECT ip FROM radfreecharge ORDER BY ip")
    data = cur.fetchall()
    return data



