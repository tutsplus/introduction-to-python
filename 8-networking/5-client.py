import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8000))
s.send("My name is Derek")
data = s.recv(1024)
print 'Received from server', data
s.close()

print 'Client is disconnected'
