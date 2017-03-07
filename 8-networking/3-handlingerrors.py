import socket
import sys

def get_info(host_name = ''):
    if(host_name == ''):
        host_name = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(host_name)

        print "Host Name = %s" % host_name
        print "IP Address = %s" % ip_address
    except socket.gaierror, e:
        print "Couldn't connect to host_name: %s - Error: %s" % (host_name, e)
    except socket.error, e:
        print "Connection error: %s" % e

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        get_info()
    else:
        get_info(sys.argv[1])
