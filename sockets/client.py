import socket

s = socket.socket()

addr = input("Enter address: ")
port = int(input("Enter port: "))

s.connect((addr, port))
print(s.recv(1024))
s.close()
