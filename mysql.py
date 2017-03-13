#!/usr/bin/python
#_*_ coding:utf-8 _*_

import MySQLdb
conn = MySQLdb.connect(host='36.189.253.147',user='srgs',passwd='srgs2016',db='proeprodb',port=33006)
cur = conn.cursor()
sql = "select ani,dnis,stopcause,begintime from callist"
cur.execute(sql)
data = cur.fetchall()
for i in data:
    print i
cur.close()
conn.close()
