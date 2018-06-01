import os


def get_ipaddr():
    ipaddr = os.popen('hostname -I').read()
    ipaddr = ipaddr.strip()
    return ipaddr
