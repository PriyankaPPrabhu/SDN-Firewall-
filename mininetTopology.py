
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.cli import CLI

class SingleSwitchTopo(Topo):
    "Single switch connected to x hosts."
    def build(self, x=2):
        switch = self.addSwitch('s1', dpid="00000000000007")
        
        for h in range(x):
            host = self.addHost('h%s' % (h + 1), ip='10.0.0.%s' % (h+1), mac='00:00:00:00:00:0%s' % (h+1))
            self.addLink(host, switch)

def simpleTest():
    
    topo = SingleSwitchTopo(x=4)
    net = Mininet(topo, controller=None)
    
    c = RemoteController('c', '0.0.0.0', 6633)
    net.addController(c)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    CLI(net)
    net.stop()

if __name__ == '__main__':
    
    setLogLevel('info')
simpleTest()
