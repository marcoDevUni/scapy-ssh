from tabnanny import verbose
from scapy.all import *
import sys

sys.path.append("./scapy/layers/")
import ssh


def a(myIP):
    p = IP(dst=myIP) / TCP(dport=22) / ssh.SSH() / ssh.SSHIdent(ident="SSH-2.0")
    p.show()
    return sr(p)


def TCPHandShake(myIP):
    ip=IP(dst=myIP)
    SYN=TCP(dport=22,flags='S',seq=1000)
    SYNACK=sr1(ip/SYN)

    # SYN-ACK
    ACK=TCP(dport=22, flags='A', seq=SYNACK.ack + 1, ack=SYNACK.seq + 1)
    return send(ip/ACK)


# def b(myIP):
#     p=IP(dst=myIP)/TCP(dport=22)/ssh.SSHMessage()/ssh.SSHKexInit(languages_client_to_server="uk",reserved=0)
#     p.show()
#     return sr(p)

myIP = "130.192.166.120"
myIP = "192.168.1.13"
risposte = TCPHandShake(myIP)

print(risposte)
