#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.6.5
# Last Modified: 2010-09-01 15:58:15

"""docstring
"""

__revision__ = '0.1'


import yaml
IP_M_resourceID_Map = 'Conf/ip_m_resourceid_map.yaml'
cmdName_alarm = 'Conf/alarm.yaml'
ip_resourceid = 'Conf/ip_resourceid.yaml'
tbName_itemID = 'Conf/tbname_itemid.yaml'
MresouceId_resourceId = 'Conf/mresourceid_resourceid.yaml'

def loadConf(conf):
    yamlconf  = file(conf, 'r')
    try:
        cmd_list = yaml.load(yamlconf)
        return cmd_list
    except yaml.scanner.ScannerError, e:
        print 'err:',e
    finally:
        yamlconf.close()

ip_M_resourceID = loadConf(IP_M_resourceID_Map)
IP_resourceID_map = loadConf(ip_resourceid)
tbName_itemID_dict = loadConf(tbName_itemID)
MresouceId_resourceId__Map = loadConf(MresouceId_resourceId)
cmdName_alarm_map = loadConf(cmdName_alarm)





