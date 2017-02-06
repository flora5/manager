#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import glob
import socket
import datetime
from SOAPpy import SOAPProxy

url = 'http://localhost:8088'
hostname = socket.gethostname()
#n = 'urn:xmethods-Temperature'
#server = SOAPProxy(url, namespace=n)
server = SOAPProxy(url)
#server.config.dumpSOAPOut = 1
#server.config.dumpSOAPIn = 1
def test():
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
        try:
            server.put_data(hostname, action, data)
        except UnicodeDecodeError, e:
            print e
            print 'data:',data
            print 'action:',action
test()

