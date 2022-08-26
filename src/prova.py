from tabnanny import verbose
from scapy.all import *
import sys

sys.path.append("./scapy/layers/")
import ssh


def a(myIP):
    p = IP(dst=myIP) / TCP(dport=22) / ssh.SSH() / ssh.SSHIdent(ident="SSH-2.0")
    return sr(p)


# def b(myIP):
#     p=IP(dst=myIP)/TCP(dport=22)/ssh.SSHMessage()/ssh.SSHKexInit(languages_client_to_server="uk",reserved=0)
#     p.show()
#     return sr(p)

myIP = "127.0.0.1"
risposte, nonRisposte = a(myIP)

print(risposte)
for risposta in risposte:
    ssh.SSH(risposta).show()


print(nonRisposte)
for risposta in nonRisposte:
   ssh.SSH(risposta).show()
