#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.6.5
# Last Modified: 2010-08-31 09:12:22

"""docstring
"""

__revision__ = '0.1'



from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol


class Manager(DatagramProtocol):

    def datagramReceived(self, data, (host, port)):
        print "received %r from %s:%d" % (data, host, port)
        savetrap(data, host)


reactor.listenUDP(8888, Manager())
reactor.run()

