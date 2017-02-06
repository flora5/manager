#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.6.5
# Last Modified: 2010-08-26 10:24:28

"""docstring
"""

__revision__ = '0.1'

import cx_Oracle
import uuid,  time, re,  sys
from re import match
import loadconf
from loadconf import IP_resourceID_map
from tableconf import tbName_column



pool = cx_Oracle.SessionPool(user='itsm', password='itsm', dsn='192.168.8.86:1521/ora10', min =1, max=10, increment=1)
db = pool.acquire()
cursor = db.cursor()
cursor.arraysize = 100



new_dict = {}
for k in tbName_column.keys():
    tmp_dict = {k[0]: tbName_column[k]}
    new_dict.update(tmp_dict)
tbattr_dict = {}
for kk in   new_dict.keys():
    attr_list = []
    for attr in  new_dict[kk]:
        attr_list.append(attr[0])
    tmp_dict = {kk: attr_list}
    tbattr_dict.update(tmp_dict)
#print tbattr_dict

time_format = "\'YYYY-MM-DD HH24:MI:SS\'"
ISOTIMEFORMAT='%Y-%m-%d %H:%M:%S'
pattern  = '\'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\''



def formatetime(s):
    return  time.strftime(ISOTIMEFORMAT, time.localtime(float(s)))
    
def save(saveDatas, tbName):
    upperTbName = tbName.upper()
    lenth = len(saveDatas[0])
    values = [str(a) for a in range(lenth+1)[1:]]
    i = 0
    for value in values:
        values[i] = ":" + values[i]
        i = i + 1
    values[-3] =  'TO_DATE(%s,%s)' %(values[-3], time_format)
    Value = tuple(values)
    columns = str(tuple([b for b in tbattr_dict[tbName]]))
    cols = ''
    for c in columns:
        if c != "'":
            cols = cols + c # can't remember what is this .........??? 
    sql = "INSERT INTO %s %s VALUES %s" %(upperTbName,cols, Value)
    sql = sql.replace("'", "")
    sql = sql.replace("\"", "")
    sql = sql.replace("YYYY-MM-DD HH24:MI:SS", "\'YYYY-MM-DD HH24:MI:SS\'")
    try:
        cursor.prepare(sql)
        cursor.executemany(None, saveDatas)
        db.commit()
    except cx_Oracle.Error, exc:
        db.rollback()
        error, = exc.args
        print "insertPool.py   %s  Oracle-Error-Code: %s Oracle-Error-Message: %s" %(time.ctime(), error.code, error.message)
        print tbName
        #f = open('errlog/oracle.log', 'a')
        #print >> f, erro
        #f.close()
    finally:
       pool.release(db) 
       #cursor.close()





