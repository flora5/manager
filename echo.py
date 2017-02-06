#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.5.2
# Last Modified: 2010-07-27 10:24:28

"""docstring
"""

__revision__ = '0.1'

from twisted.internet import reactor, defer
#from twisted.internet import epollreactor
#epollreactor.install()
#from twisted.internet.protocol import Protocol, Factory, ClientFactory, ServerFactory
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver

import os
import time
from subprocess import *
import StringIO
import yaml


fd = open("log2/start.list", "r")
dd = fd.read()
fd.close()
CONFIG = yaml.load(dd)

def DEFERRED(func):
    def xx(*args, **argv):
        d = defer.Deferred()
        d.callback(func(*args, **argv))
        return d
    return xx

#@DEFERRED
def getProcessOutput(args):
    d = deferred = defer.Deferred()
    sp = Popen(args, stdout=PIPE, stderr=PIPE, shell=True, bufsize=0)
    sp.wait()
    if sp.returncode != 0:
        d.callback('')
        return d
    data = sp.stdout.read()
    d.callback(data)
    return d
#    return data

class YamlAgent(LineReceiver):
    delimiter = '\n'
    def connectionMade(self):
        print"Connected from", self.transport.client
        self.yamldata =''
        #self.transport.write('<hits>')

    def connectionLost(self, reason):
        print"Disconnected from", self.transport.client

    def lineReceived(self, line):
        """As soon as any data is all received, parse it and write back."""
        print 'data received:', line
        self.yamldata += line + '\n'
        if line == '---':
            self.yamldata = ''
        if line == '...':
            print "yaml:", self.yamldata
            try:
                data = yaml.load(self.yamldata)
            except yaml.scanner.ScannerError, e:
                print 'err:',e
                self.transport.write(yaml.dump({'response':'%s'%e,'returncode':400,'time:':int(time.time())})+'...\n')
                return None
            finally:
                self.yamldata = ''
            try:
                action = data['action']            #get, getnext, ...
                description = data['description']
                script = ''.join((action, '_', description))
            except KeyError, e:
                self.transport.write(yaml.dump({'response':'%s'%e,'returncode':401,'time:':int(time.time())})+'...\n')
                return None
            try:
                if isinstance(data['status'], list):
                    status = [str(d) for d in data['status']]
                else:
                    status = [str(data['status'])]
            except KeyError, e:
                status = []
            species = CONFIG.get(description)
            command = [os.path.join('log2', species, script),] + status
            print 'command:', command
            getProcessOutput(command,
                    ).addCallback(self.dumpPDU
                    ).addCallback(self.transport.write)

    def writeT(self, d):
        data = {'returncode':0,'time:':int(time.time())}.update(d)
        self.transport.write(yaml.dump(data)+'...\n')

    def dumpPDU(self, y):
        buff = []
        #lines = y.split('\n')
        for line in StringIO.StringIO(y).readlines():
            buff.append(line.split())
        #print 'buff:', buff
        return yaml.dump({'response':buff,'returncode':0,'time:':int(time.time())}) + '...\n'


f = ServerFactory()
f.protocol = YamlAgent

#def main():
#    reactor.listenTCP(8000, f)
#    reactor.run()
#
#
#if __name__ == '__main__':
#    #main()
#    pass
from twisted.application import internet, service
application = service.Application('test_service')
testService = internet.TCPServer(8800, f)
testService.setServiceParent(application)

