from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory, Protocol


class Client(Protocol):
    def connectionMade(self):
        print "good"
        self.transport.write("111")
        self.transport.loseConnection()

class ListenerFactory(ClientFactory):
    protocol = Client


reactor.connectTCP("127.0.0.1", 8008, ListenerFactory())
reactor.run()
