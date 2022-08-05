from scapy.all import *

import logging
logger = logging.getLogger("scapy")
logger.setLevel(logging.INFO)


def vlenq2str(l):
    s = []
    s.append(l & 0x7F)
    l = l >> 7
    while l > 0:
        s.append(0x80 | (l & 0x7F))
        l = l >> 7
    s.reverse()
    return bytes(bytearray(s))


def str2vlenq(s=b""):
    i = l = 0
    while i < len(s) and ord(s[i:i+1]) & 0x80:
        l = l << 7
        l = l + (ord(s[i:i+1]) & 0x7F)
        i = i + 1
    if i == len(s):
        warning("Broken vlenq: no ending byte")
    l = l << 7
    l = l + (ord(s[i:i+1]) & 0x7F)

    return s[i+1:], l


class VarLenQField(Field):
    """ variable length quantities """
    __slots__ = ["fld"]

    def __init__(self, name, default, fld):
        Field.__init__(self, name, default)
        self.fld = fld

    def i2m(self, pkt, x):
        if x is None:
            f = pkt.get_field(self.fld)
            x = f.i2len(pkt, pkt.getfieldval(self.fld))
            x = vlenq2str(x)
        return raw(x)

    def m2i(self, pkt, x):
        if s is None:
            return None, 0
        return str2vlenq(x)[1]

    def addfield(self, pkt, s, val):
        return s+self.i2m(pkt, val)

    def getfield(self, pkt, s):
        return str2vlenq(s)


class FOO(Packet):
    name = "FOO"
    fields_desc = [VarLenQField("len", None, "data"),
                   StrLenField("data", "", length_from=lambda pkt: pkt.len)]

bind_layers(TCP, FOO, sport=22)
bind_layers(TCP, FOO, dport=22)
