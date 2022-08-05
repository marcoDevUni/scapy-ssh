def prova():

    # for local testing only ---->
    p = IP(dst="130.192.166.120")/TCP(dport=22)/SSH()/SSHIdent(ident="SSH-2.0-x\r\n")

    # IP(dst="130.192.166.120")
    # p = IP(dst="130.192.166.120")/TCP(dport=22)/SSHKexInit( \
        # encryption_algorithms_client_to_server=SSH_ALGO_CIPHERS[0], \
        # encryption_algorithms_server_to_client=SSH_ALGO_CIPHERS[0], \
        # kex_algorithms=SSH_ALGO_CIPHERS[0], \
    #    languages_client_to_server="de,uk,de,uk", \
        # languages_client_to_server_length=999,\
        # languages_server_to_client="xx", \
        # kex_first_packet_follows=2, \
    #    reserved=0) \
        # /('a'*100)
    ans = send(p)


if __name__ == "__main__":
    from scapy.all import *
    import sys
    sys.path.append("scapy/layers")
    from ssh import *

    interact(mydict=globals(), mybanner="Test add-on v3.14")
