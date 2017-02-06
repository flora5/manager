from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
import subprocess

class Listener(Protocol):
    def dataReceived(self,data):
        print "hello",  data
        if data == "111":
            print " table has been changed run read_db now ..."
            subprocess.call(['python','read_db.py'])


class ListenerFactory(Factory):
    protocol = Listener

reactor.listenTCP(8008, ListenerFactory())
reactor.run()
