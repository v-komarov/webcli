#coding:utf-8

import pytest
import MySQLdb
import datetime
from src.conf import mysql_host, mysql_user, mysql_passwd, mysql_db
from src.db import wlog


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


def test_radpackets():
    """count of table radpackets"""
    conn = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM radpackets")
    assert cur.fetchone()[0] != 0




def test_writing_log_pre():
    """Checking writing log"""
    conn = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)
    cur = conn.cursor()
    cur.execute("DELETE FROM user_logs")
    conn.commit()
    cur.execute("SELECT count(*) FROM user_logs")
    assert cur.fetchone()[0] == 0



def test_writing_log():
    """Checking writing log"""
    wlog('testuser','xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    conn = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM user_logs WHERE username='testuser'")
    assert cur.fetchone()[0] == 1



def test_writing_mac_pre():
    """Checking writing mac"""
    conn = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)
    cur = conn.cursor()
    cur.execute("DELETE FROM macs_tmp")
    conn.commit()
    cur.execute("SELECT count(*) FROM macs_tmp")
    assert cur.fetchone()[0] == 0


def test_writing_mac():
    """Checking writing mac"""
    conn = MySQLdb.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)
    cur = conn.cursor()
    cur.execute("""CALL writemac(%s,%s)""", ('08C6B32B3D04',datetime.datetime.now()))
    conn.commit()
    cur.execute("SELECT count(*) FROM macs_tmp")
    assert cur.fetchone()[0] == 1

