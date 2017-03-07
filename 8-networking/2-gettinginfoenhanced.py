import socket
import sys

def get_info(host_name = ''):
    if(host_name == ''):
        host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)

    print "Host Name = %s" % host_name
    print "IP Address = %s" % ip_address

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        get_info()
    else:
        get_info(sys.argv[1])
