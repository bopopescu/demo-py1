import socket

mysocket = socket.socket()
mysocket.bind(('',30035))

mysocket.listen(5)

while True:
    conn,addr = mysocket.accept()
    print("address to listen",addr)
    conn.send(b'handshake message.')
    conn.close()

"""
[prave@localhost ~]$ telnet localhost 30030
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Connection closed by foreign host.
[prave@localhost ~]$ telnet localhost 30030
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
handshake message.Connection closed by foreign host.
[prave@localhost ~]$ telnet www.google.com 80
Trying 172.217.163.132...
Connected to www.google.com.
Escape character is '^]'.
Connection closed by foreign host.
[prave@localhost ~]$

"""