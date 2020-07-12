import socket

ip = socket.gethostbyname("www.google.com")
addr = socket.gethostbyaddr("www.google.com")

print(ip)
print(addr)