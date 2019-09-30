#coding:utf-8

import pytest
import MySQLdb
from src.conf import mysql_host, mysql_user, mysql_passwd, mysql_db



def test_conn():
    """Check connect to mysql server"""
    conn = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)
    cur = conn.cursor()
    cur.execute("SELECT 1")
    assert cur.fetchone()[0] == 1


def test_freechanals():
    """count of table radfreecharge"""
    conn = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM radfreecharge")
    assert cur.fetchone()[0] != 0

