#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.6.5
# Last Modified: 2010-09-03 16:55:09

"""docstring
"""

__revision__ = '0.1'

import os, time, uuid, sys, socket
import  yaml , cx_Oracle
from multiprocessing import Process, Pool
from uncompress import auto_uncompress
from loadconf import ip_M_resourceID
import alarm, insertPool


TIMEOUT = 1
delimiter = '\n'
PORT = 8800
_all = ''
ISOTIMEFORMAT='%Y-%m-%d %H:%M:%S'


def formatetime(s):
    return  time.strftime(ISOTIMEFORMAT, time.localtime(float(s)))

def save2Oracle(yamldata, tbName, M_resource_id, item_name):
    if yamldata['response'] == []:
        print "Agent returned nothing"
    else:
    #elif yamldata['compressed'] == None:
        saveDatas = yamldata['response']
        gathertime = yamldata['time:']
        gatherTime = formatetime(gathertime)
        for savedata in saveDatas:
            savedata.append(gatherTime)
            savedata.append(M_resource_id)
            savedata.append(str(uuid.uuid1()))
            alarm.is_alarm(savedata, tbName,item_name)
        insertPool.save(saveDatas, tbName)
    #elif yamldata['compressed'] != None:
        #print "data are compressed !", yamldata['compressed']
        # auto_uncompress()

def yaml_load(data):
    try:
        yamldata = yaml.load(data)
        return yamldata
    except yaml.scanner.ScannerError, e:
        err = "%s manager.py line 40 yaml load error: %s" %(time.ctime(), e)
        f = open('errlog/error.log', 'a')
        print >> f, err
        f.close()
        return None




def manager(value_list):
    item_name = value_list[-1]
    for HOST in value_list[:-3] :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        try:
            s.connect((HOST, PORT))
        except:
            alarm.host_counter(HOST)
            break
        alarm.remove_host(HOST)
        _all = ''
        cmd = {"action": "get", "description": item_name}
        sendline =yaml.dump(cmd) + '...\n'
        s.send(sendline)
        s.settimeout(2)
        while '...' not in _all:
            try:
                data = s.recv(1024)
            except:
                print "time out",  HOST
                _all = ''
                break
            _all = _all + data
        yamldata = yaml_load(_all)
        if yamldata:
            print yamldata
            M_resource_id = ip_M_resourceID[HOST]
            tbName = value_list[-3]
            save2Oracle(yamldata, tbName, M_resource_id, item_name)
            _all = ""
        s.close()


def is_run():
    isrun = file('Conf/isrun.yaml', 'r')
    run_num = yaml.load(isrun)
    return run_num
    isrun.close()



# cpu nan

if __name__ == '__main__':

    while 1:
        start = time.time()
        run_num = is_run()
        if run_num == '[1]':
            print  "manager start..."
            stream = file('Conf/fliter.yaml', 'r')
            fliter_cmdinfo = yaml.load(stream)
            pro_pool = Pool(processes=6)
            host_list = []
            i = 0
            for item_name in fliter_cmdinfo.keys():
                if fliter_cmdinfo[item_name] != []:
                    tmp_list = fliter_cmdinfo[item_name]
                    host_list.append(tmp_list)
                host_list[i].append(item_name)
                i = i+1
            pro_pool.map(manager, host_list)
            print  time.time() - start
            time.sleep(1)
        else:
            print "manager stoped"
            sys.exit()









#null  nan
#...
#8.135: 1}
