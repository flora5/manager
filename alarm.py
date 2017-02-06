#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.6.5
# Last Modified: 2010-09-03 16:02:57

"""docstring
"""

__revision__ = '0.1'


import cx_Oracle
from loadconf import  tbName_itemID_dict, MresouceId_resourceId__Map,cmdName_alarm_map, IP_resourceID_map
import time, yaml
import uuid

#db = cx_Oracle.connect('itsm', 'itsm', '192.168.8.86:1521/ora10')
#cursor = db.cursor()

pool = cx_Oracle.SessionPool(user='itsm', password='itsm', 
                             dsn='192.168.8.86:1521/ora10',
                             min =1, max=10,
                             increment=1, 
                             connectiontype=cx_Oracle.Connection, 
                             getmode = cx_Oracle.SPOOL_ATTRVAL_NOWAIT)      

# getmode=cx_Oracle.SPOOL_ATTRVAL_NOWAIT                    


time_format = "\'YYYY-MM-DD HH24:MI:SS\'"
# savedata[3]  number is index

ISOTIMEFORMAT='%Y-%m-%d %H:%M:%S'
def formatetime(s):
    return  time.strftime(ISOTIMEFORMAT, time.localtime(float(s)))


alarm_map = {'monitor_item_disk': 3,'monitor_item_memory': 2,'monitor_item_processes':8,'monitor_item_swap': 2} # this should get from database

def is_alarm(savedata, tbName, item_name):
    serious = cmdName_alarm_map[item_name][0]
    common = cmdName_alarm_map[item_name][1]
    if tbName in alarm_map.keys():
        alarm_index = alarm_map[tbName]
        if savedata[alarm_index] > serious:
            info = "严重告警"
            save_alarm(savedata, tbName, item_name, info)
        elif savedata[alarm_index] > common:
            info = "普通告警 "
            save_alarm(savedata, tbName, item_name, info)





def save_alarm(savedata, tbName, item_name, info):
    connection1 = pool.acquire()
    cursor = connection1.cursor()
    en_cn_map = {'disk_space': "磁盘",  'memory_performance': "内存",  'processes_snapshot': "进程cpu占用率", 'swap_space': "交换分区"}
    if item_name == 'processes_snapshot':
        alert_msg = "%s超标"%(en_cn_map['processes_snapshot'])
    else:
        alert_msg = "%s 空间不足"%(en_cn_map[item_name])
    alert_name = "%s 告警" %(en_cn_map[item_name])
    alarm = "insert into ALERT_INFO (INFO_ID,RESOURCE_ID,ITEM_ID,ALERT_TIME,ALERT_MESSAGE,ALERT_NAME,IS_INTERMIT,REMARK) values('%s','%s','%s',TO_DATE('%s',%s),'%s','%s','1','%s')" %(savedata[-1],savedata[-2], tbName_itemID_dict[tbName], savedata[-3], time_format, alert_msg, alert_name, info)
    alarm = unicode(alarm,'utf8').encode('GBK')
    try:
        cursor.execute(alarm)
        connection1.commit()
    except cx_Oracle.Error, exc:
        connection1.rollback()
        error,  = exc.args
        print  "%s alarm.py Oracle-Error-Code: %s Oracle-Error-Message: %s" %(time.ctime(), error.code, error.message)
        print tb_name
        #f = open('errlog/oracle.log', 'a')
        #print >> f, c
        #f.close()
    finally:
        pool.release(connection1)



def host_donwn_warn(host):
    connection2 = pool.acquire()
    cursor = connection2.cursor()
    for map in IP_resourceID_map:
        if host in map[0]:
            resource_id = map[1]
            uid =str(uuid.uuid1())
            atime = time.time()
            alarm_time = formatetime(atime)
            ins = "INSERT INTO ALERT_INFO (INFO_ID,IS_INTERMIT,ALERT_MESSAGE,RESOURCE_ID,ALERT_TIME) VALUES ('%s','0', '无法连接到该主机 %s','%s',TO_DATE('%s',%s))" %(uid, host, resource_id, alarm_time, time_format)
            ins = unicode(ins,'utf8').encode('GBK')
            print ins
            try:
                cursor.execute(ins)
                connection2.commit()
                #print "good host down info saved"
                
            except cx_Oracle.Error, exc:
                connection2.rollback()
                error,  = exc.args
                c = "%s alarm.py Oracle-Error-Code: %s Oracle-Error-Message: %s" %(time.ctime(), error.code, error.message)
                f = open('errlog/oracle.log', 'a')
                print >> f, c
                f.close()
            finally:
                pool.release(connection2)



# following methodes just used to incase of keep alarming the off-host
# has nothing to do with the connection thing
# so the program still try to make connection with all the host which in the timeup.yaml file
# during the 20 minute it still work though

def dump_count(data):
    stream = file('Conf/host_down_counter.yaml', 'w')
    counter = yaml.dump(data, stream)

def load_count():
    stream = file('Conf/host_down_counter.yaml', 'r')
    counter = yaml.load(stream)
    return counter

def remove_host(host):
    counter = load_count()
    if counter and host in counter.keys():
        counter.pop(host)
        data = counter
        dump_count(data)



def host_counter(host):
    max_counter = 50
    counter = load_count()
    if counter == None:
        data = {host: 1}
        dump_count(data)
        host_donwn_warn(host)
    elif host not in counter.keys():
        tmp_dict  = {host: 1}
        data  = counter.update(tmp_dict)
        dump_count(data)
        host_donwn_warn(host)
    elif counter[host] ==1:
        host_donwn_warn(host)
        counter[host] =  counter[host] + 1
        data = counter
        dump_count(data)
    elif counter[host] >1 and counter[host]< max_counter:
        counter[host] =  counter[host] + 1
        data = counter
        dump_count(data)
    elif counter[host]>= max_counter:
            counter.pop(host)

# befor remove down hosts from  timeup_file  capy it to another file ----inclue where is came from and it's time line
# after 20minit we write it back to timeup_file it it still in runing time
# this gonna save a lot of time ...................






