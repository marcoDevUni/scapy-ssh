#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Author : tintinweb@oststrom.com <github.com/tintinweb>


def padding_fix(p):
    padd= 8-len(p)%8
    if p.haslayer(Raw):
        p[Raw].load += 'P'*padd
    else:
        p=p/('P'*padd)
    return p

if __name__=="__main__":
    from scapy.all import *
    
    # for local testing only ---->
    import ssh2 as sshcustom
    import socket

    target = ('130.192.166.120',22) 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(target)
    
    p = sshcustom.SSH()/sshcustom.SSHIdent(ident="SSH-2.0-")       # missing \r\n
    
    p.show()
    
    
    print("sending payload")
    print(str(p))
    # s.sendall(str(p))
    
    # resp = s.recv(1024)
    # print("received, %s"%repr(resp))
    # sshcustom.SSH(resp).show()
    
    # s.close()
