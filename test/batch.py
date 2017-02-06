#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.6.5
# Last Modified: 2010-08-26 10:24:28

"""docstring
"""

__revision__ = '0.1'


import cx_Oracle
import uuid,  time, re
from re import match
import loadconf
from loadconf import IP_resourceID_map
from tableconf import tbName_column

#db = cx_Oracle.connect('itsm', 'itsm', '192.168.8.86:1521/ora10') # not in use


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
def formatetime(s):
    return  time.strftime(ISOTIMEFORMAT, time.localtime(float(s)))
pattern  = '\'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\''


def save(data, tbName):
    pool = cx_Oracle.SessionPool(user='itsm', password='itsm', dsn='192.168.8.86:1521/ora10', min =1, max=6, increment=1)
    db = pool.acquire()
    cursor = db.cursor()
    cursor.arraysize = 100
    
    upperTbName = tbName.upper()
    values = str(tuple([a for a in data]))
    coll =  tuple([b for b in tbattr_dict[tbName]])
    columns = str(tuple([b for b in tbattr_dict[tbName]]))
    cols = ''
    for c in columns:
        if c != "'":
            cols = cols + c
    aa = "INSERT INTO %s %s VALUES %s" %(upperTbName,cols, values)
    match = re.search(pattern,aa) #
    resoult = match.group()
    target = 'TO_DATE(%s,%s)' %(resoult, time_format)
    formated_sql = re.sub(pattern, target,aa) #
    print formated_sql
    try:
        cursor.execute(formated_sql)
        cursor.execute('commit')
        print "ok=======================ok", tbName 
    except:
        print "failed to insert data", values  # >> insertErrLog.txt 
    finally:
        pool.release(db)

