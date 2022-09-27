#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    net = Mininet( topo=None, build=False )

    info( '*** Adding controller\n' )
    
    net.addController('c0', controller=RemoteController,ip="127.0.0.1",port=6633)
    
    info( '*** Adding hosts\n' )
    hosts=[]
    for h in range(50):#change here for number of hosts
	hosts.append('h%s' % (h+1))

    info( '*** Adding switch\n' )
    
   
    switches = []
    for i in range(6): #change here for number of switches
	switches.append('s%d' % (i+1))
    

    for h in hosts: #create hosts
	globals() [h]= net.addHost(h)

    for s in switches:#create switches
	globals() [s] = net.addSwitch(s, cls=OVSSwitch)
	

    info( '*** Creating links\n' )
   
    i=n=0;

    for h in hosts:
	net.addLink(h,switches[i])
	n+=1
	if(n==10):#number of host per switch
		i+=1
		n=0

    ## switches
    
    net.addLink(s1,s6)
    net.addLink(s2,s6)
    net.addLink(s3,s6)
    net.addLink(s4,s6)
    net.addLink(s5,s6)

    net.addLink(s1,s2)
    net.addLink(s2,s3)
    net.addLink(s3,s4)
    net.addLink(s4,s5)
    net.addLink(s5,s1)

    info( '*** Starting network\n')
    net.start()

    #info('*** Set ip address to switch\n')
    

    #info('*** Enable spanning tree\n') 
    for s in switches:                  
    	globals() [s].cmd('ovs-vsctl set bridge %s stp-enable=true' % (s))
    	

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
