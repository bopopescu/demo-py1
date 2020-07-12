import socket

myclient = socket.socket()

#myclient.connect(('localhost',30030))
myclient.connect(('127.0.0.1',30035))

print(myclient.recv(1024))

myclient.close()