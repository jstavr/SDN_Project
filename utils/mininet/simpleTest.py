#!/usr/bin/env python


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
import random



    
PORT_TYPE_MULTIPLIER = 10000
SWITCH_ID_MULTIPLIER = 100000

class randomTopo(Topo):
    "A random topology of n switches, where each switch has between p and r hosts connected to it"

    
    def __init__(self, n=4, p=1, r=5l):
        Topo.__init__(self)
        hostCnt = 0
        oldSwitch = None
        allSwitches = []
        for s in range(n):
            switch = self.addSwitch('s%s' % (s + 1))
            allSwitches.append(switch)
            if oldSwitch and random.random()>0:
                self.addLink(switch, oldSwitch)
            for h in range(random.randint(p, r)):
                host = self.addHost('h%s' % (hostCnt + 1))
                hostCnt+=1
                self.addLink(host, switch)
            oldSwitch = switch


        self.generate_backbone_tf("test.out")
    def generate_backbone_tf(self, dest_path):
        output = ""
        ports = []
        for (src, dst) in self.links():
            if src in self.switches() and dst in self.switches():
                ports.append((src, dst, self.port(src, dst)))



        cnt = 1
        for (src, dst, tpl) in ports:
            src_flat = int(src[1:]) * SWITCH_ID_MULTIPLIER + tpl[0]
            dst_flat = int(dst[1:]) * SWITCH_ID_MULTIPLIER + tpl[1]
            output += "link$[" + str(src_flat) + "]$None$None$None$None$None$[" + str(dst_flat) + "]$#$#$$$_" + str(cnt) + "\n"
            cnt+=1

        f = open(dest_path, 'w')
        f.write(output)
        f.close()


#        for s in self.switches():
#            for ss in self.switches():
#                if random.random()>0:
#                    alreadyLinked = False
#                    for l in self.links():
#                        if (s in l) and (ss in l):
#                            alreadyLinked = True

#                    if not alreadyLinked:
#                        self.addLink(s, ss)
                    

topos = { 'randomTopo' : (lambda : randomTopo() ) }            
            



class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)




def simpleTest():
    "Create and test a simple network"
    topo = randomTopo(n=4, p=1, r=7)
    net = Mininet(topo, controller=RemoteController('c0', ip='10.0.0.11', port=6653))
#    net.addController('c0', controller=RemoteController, ip='10.0.0.11', port = 6653)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
#    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
