#coding:utf-8

import os

auth_service = os.environ.get('AUTH_SERVICE','10.6.0.22:8000/begin/jsondata/')

mysql_host = os.environ.get('MYSQL_HOST', '127.0.0.1')

mysql_user = os.environ.get('MYSQL_USER', 'freeradius')

mysql_passwd = os.environ.get('MYSQL_PASSWORD', 'freeradius')

mysql_db = os.environ.get('MYSQL_DB', 'radius')

radtest_host = os.environ.get('RADTEST_HOST', '127.0.0.1')

radtest_port = os.environ.get('RADTEST_PORT', '8080')

