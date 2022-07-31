from scapy.all import *


class StrCustomTerminatorField(StrField):

    def __init__(self, name, default, fmt="H", remain=0, terminator="\x00\x00", consume_terminator=True):
        super().__init__(name, default, fmt, remain)

        self.terminator = terminator
        self.consume_terminator = consume_terminator


StrCustomTerminatorField(
    "language", "",
    terminator="\x00", consume_terminator=False),
