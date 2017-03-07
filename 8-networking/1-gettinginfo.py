import socket

def get_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)

    print "Host Name = %s" % host_name
    print "IP Address = %s" % ip_address

if __name__ == '__main__':
    get_info()
