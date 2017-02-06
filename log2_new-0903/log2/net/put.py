#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import glob
import socket
import datetime
import conf

hostname = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def put_sys_info():
    #print 'host:', sys.argv[1]
    #print 'PORT:', sys.argv[2]
    #print 'user:', sys.argv[3]
    #print 'pass:', sys.argv[4]
    for f in glob.glob("upload/get*"):
        action = os.path.split(f)[1]
        fd = open(f)
        data = fd.read().split()
        fd.close()
        try:
            data = [datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),] + data[1:]
        except IndexError, e:
            pass
        #print 'host:',hostname
        #print 'action:',action
        #print 'data:',data
        data = '|'.join(data)
        data = '|'.join((hostname,action,data))
        #print 'data:',data
        try:
            #server.put_data(hostname, action, data)
            #sock.sendto(data, ('localhost', 9999))
            sock.sendto(data, conf.server_ip)
        except UnicodeDecodeError, e:
            print e
            print 'data:',data
            print 'action:',action
        except socket.error, e:
            print e
            print 'data:',data
            print 'action:',action

put_sys_info()

