from scapy.all import *
import sys
sys.path.append("scapy/layers")
from ssh import *

def a():
    # p = IP(dst="130.192.166.120")/TCP(dport=22)/SSH()/SSHIdent(ident="SSH-2.0-x\r\n")
    p=IP(dst="130.192.166.120")/TCP(dport=22)/SSH()
    pkt, altro = sr(p)
    return SSH(pkt)


def b():
    # p = IP(dst="130.192.166.120")/TCP(dport=22)/SSH()/SSHIdent(ident="SSH-2.0-x\r\n")
    p=IP(dst="130.192.166.120")/TCP(dport=22)/SSHMessage()/SSHKexInit(
        languages_client_to_server="de,uk,de,uk", 
        reserved=0) 
        
    pkt, altro = sr(p)
    return SSH(pkt)

x=b()
x.show()