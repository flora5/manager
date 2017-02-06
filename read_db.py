#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.6.5
# Last Modified: 2010-08-26 10:24:28

import cx_Oracle, time, csv
import threading, sched, yaml


itemid_cmd_map = {'001': 'all_users',
                                '002': 'memory_performance', 
                                '003': 'disk_space', 
                                '004': 'cpu_performance',
                                '005': 'processes_snapshot',
                                '006': 'swap_space'}
                                

db = cx_Oracle.connect('itsm', 'itsm', '192.168.8.86:1521/ora10')
cursor = db.cursor()

get_mission_id = "SELECT MISSION_ID FROM MONITOR_MISSION"
get_mresource_id = "SELECT MRESOURCE_ID FROM MONITOR_MISSION_RESOURCE WHERE MISSION_ID IN (%s)" %(get_mission_id)
#get_resource_id = "SELECT RESOURCE_ID FROM MONITOR_RESOURCE WHERE MRESOURCE_ID IN (%s)" %(get_mresource_id)
get_mitem_id = "SELECT DISTINCT ITEM_ID FROM MONITOR_RESOURCE_ITEM WHERE MRESOURCE_ID IN (%s)" %(get_mresource_id)

cursor.execute(get_mitem_id)
mitem_id_list = cursor.fetchall()

itemid_num = []
for x in mitem_id_list:
    if x[0] in itemid_cmd_map.keys():
        itemid_num.append(x[0])

mitemid_many_ip = {}
for itemid in itemid_num:
    get_mresourceid = "SELECT MRESOURCE_ID FROM MONITOR_RESOURCE_ITEM WHERE ITEM_ID = '%s'" %(itemid)
    get_resourceid = "SELECT RESOURCE_ID FROM MONITOR_RESOURCE WHERE MRESOURCE_ID IN (%s)" %(get_mresourceid)
    get_ip = "SELECT IP_ADDRESS FROM NETWORK_ADDRESS where RESOURCE_ID IN (%s)"%(get_resourceid) 
    cursor.execute(get_ip)
    tmp_dict = {itemid: cursor.fetchall()}
    mitemid_many_ip.update(tmp_dict)
#print  mitemid_many_ip

for item_id in mitemid_many_ip.keys():
    get_tbname_timegap = "SELECT MONITOR_ITEM.TABLE_NAME, MONITOR_STRATEGY.CINTERVAL_TIME \
                        FROM MONITOR_ITEM,MONITOR_STRATEGY \
                        WHERE MONITOR_ITEM.ITEM_ID = '%s' \
                        AND MONITOR_STRATEGY.STRATEGY_ID \
                        IN (SELECT STRATEGY_ID FROM MONITOR_ITEM WHERE ITEM_ID = '%s')" %(item_id,  item_id)

    cursor.execute(get_tbname_timegap)
    result = cursor.fetchone()
    mitemid_many_ip[item_id].append(result)
#print mitemid_many_ip

itemname_many_ip = {}
for mitemid in mitemid_many_ip :
    if mitemid in itemid_cmd_map.keys():
        tmp_dict = {itemid_cmd_map[mitemid]: mitemid_many_ip[mitemid]}
        itemname_many_ip.update(tmp_dict)
#print itemname_many_ip

itemname_ips = {}
for k in itemname_many_ip.keys():
    v = itemname_many_ip[k]
    tmp_tuple = ()
    for each_tuple in v:
        tmp_tuple = tmp_tuple + each_tuple
    tmp_dict = {k: list(tmp_tuple)}
    itemname_ips.update(tmp_dict)

#print  itemname_ips
stream = file('Conf/Conf.yaml', 'w')  # befor filter
yaml.dump(itemname_ips, stream) 




get_ip_mresourceid = "select network_address.ip_address, MONITOR_RESOURCE.MRESOURCE_ID \
                    from network_address, MONITOR_RESOURCE \
                    where MONITOR_RESOURCE.RESOURCE_ID = network_address.RESOURCE_ID"

cursor.execute(get_ip_mresourceid)
ip_m_resourceid_map = {}
for row in cursor:
    tmp_dict = {row[0] : row[1]}
    ip_m_resourceid_map.update(tmp_dict)

#print  ip_m_resourceid_map
stream = file('Conf/ip_m_resourceid_map.yaml', 'w')
yaml.dump(ip_m_resourceid_map, stream)

# arlam ===============================

itemid_alarm_map = {}
for mitemid in  itemid_num:  # itemid_num
    getAlarm = "SELECT MONITOR_ITEM.ITEM_ID, MONITOR_STRATEGY.SERIOUS_ALERT, MONITOR_STRATEGY.COMMON_ALERT \
            FROM MONITOR_ITEM ,MONITOR_STRATEGY WHERE \
            MONITOR_ITEM.STRATEGY_ID = MONITOR_STRATEGY.STRATEGY_ID \
            AND MONITOR_ITEM.ITEM_ID = '%s'" %(mitemid)

    cursor.execute(getAlarm)
    for row in cursor:
        serious_alarm = row[1]
        common_alarm = row[2]
        tmp_dict = {row[0]: [serious_alarm, common_alarm]}
        itemid_alarm_map.update(tmp_dict)
#print itemid_alarm_map

cmdName_alarm_map = {}
for x in itemid_alarm_map.keys():
    if x in itemid_cmd_map.keys():
        tmp_dict = {itemid_cmd_map[x]: itemid_alarm_map[x]}
        cmdName_alarm_map.update(tmp_dict)
#print cmdName_alarm_map



stream = file('Conf/Alarm.yaml', 'w')
yaml.dump(cmdName_alarm_map, stream)


tbname_itemid_dict = {}
tbName_itemID = "select TABLE_NAME,ITEM_ID from MONITOR_ITEM"
cursor.execute(tbName_itemID)
for row in cursor:
    tmp_dict = {row[0]: row[1]}
    tbname_itemid_dict.update(tmp_dict)
#print tbname_itemid_dict

stream = file('Conf/tbName_itemId.yaml', 'w')
yaml.dump(tbname_itemid_dict, stream)


missionid_time = {}
get_gather_time = "SELECT MISSION_ID,ROUND(TO_NUMBER(BEGIN_TIME-SYSDATE)*24*60*60),\
                  ROUND(TO_NUMBER(END_TIME-SYSDATE)*24*60*60) FROM MONITOR_MISSION"

cursor.execute(get_gather_time)
for row in cursor:
    tmp_dict = {row[0]:[row[1], row[2]]}
    missionid_time.update(tmp_dict)

#print missionid_time


missionID = "SELECT MISSION_ID FROM MONITOR_MISSION"
cursor.execute(missionID)
missionid_list = cursor.fetchall()

missionid_ips = {}
for x in missionid_list:
    get_ips = "select ip_address from network_address where resource_id in \
            (SELECT RESOURCE_ID FROM MONITOR_RESOURCE WHERE MRESOURCE_ID IN \
            (select MRESOURCE_ID FROM MONITOR_MISSION_RESOURCE WHERE MISSION_ID ='%s'))" %(x[0])

    cursor.execute(get_ips)
    ips = cursor.fetchall()
    tmp_dict = {x: ips}
    missionid_ips.update(tmp_dict)
#print missionid_ips

# =================timer ==============

# 数据库扫描动态增加和修改任务 对与读入的任务是透明的 
#  map的列表真是个问题 .....  

standard = itemname_ips
basic_cmd = {}
for k in standard.keys():
    tmp_dict = {k:[standard[k][-2], standard[k][-1] ]}
    basic_cmd.update(tmp_dict)




def add_ip(ips):  
    print "here is add_ip"
    for ip in ips:
        for k in standard.keys():
            if ip[0] in standard[k][:-2]: 
                basic_cmd[k].insert(0, ip[0])
   # print basic_cmd

    for k in basic_cmd.keys():
        basic_cmd[k] = list(set(basic_cmd[k][:-2])) + basic_cmd[k][-2:]  # non repeat
    #print basic_cmd
    stream = file('Conf/timeup_ips.yaml', 'w')
    yaml.dump(basic_cmd, stream)


def remove_ip(ips):
    print "here is remove ip"
    for v in basic_cmd.values():
        for ip in ips:
            if ip in v:
                v.pop(v.index(ip))
        stream = file('Conf/timeup_ips.yaml', 'w')
        yaml.dump(basic_cmd, stream)

# ======== start from here ================



s = sched.scheduler(time.time, time.sleep)
for k in missionid_time.keys():
    s_time = missionid_time[k][0]
    e_time = missionid_time[k][1]
    print s_time
    print e_time
    if s_time < 0 and e_time > 0:
        s_time = 3
    if (k, ) in missionid_list:
        ips = missionid_ips[(k, )]
        s.enter(s_time, 1, add_ip,(ips,))
        s.enter(e_time, 3, remove_ip,(ips, ))
s.run()



db.close()
