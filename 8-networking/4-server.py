import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8000))
print 'Listening for connections...'
s.listen(1)

connection, address = s.accept()
print 'Connected to client', address

while 1:
    data = connection.recv(1024)
    if not data: break
    print 'Received from client:', data
    connection.send(data)

connection.close()
