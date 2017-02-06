#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.6.5
# Last Modified: 2010-08-31 09:00:21

"""docstring
"""

__revision__ = '0.1'


from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

delimiter = '\n'

def save_to_file(log_line):
    log_file = open('logfile', 'a')
    try:
        log_file.write(log_line)
    except:
        print "failed to save line %s:" %(line)
    finally:
        log_file.close()
def save_to_oracle(parsed_log):
	pass

class SysLogReceiver(LineReceiver):
    catch = ''
    def connectionMade(self):
        self.transport.write("hello")

    def dataReceived(self, data):
        print data
        line = data + delimiter
        self.catch = self.catch + line
        catch_len = len(self.catch)
        if  catch_len >= 102:
            save_to_file(self.catch)
            self.catch = ''
    def connectionLost(self, reason):
        if self.catch:
            save_to_file(self.catch)
            self.catch = ''
            print  "bye"
        


class SysLogFactory(Factory):

    protocol = SysLogReceiver

reactor.listenTCP(5114, SysLogFactory())
reactor.run()


