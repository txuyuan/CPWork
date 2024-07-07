import socket
my_socket = socket.socket()
my_socket.bind(('127.0.0.1',3036))
my_socket.listen()
user, addr = my_socket.accept()


# Sarah states the number


while True:
    data = b''
    while b'\n' not in data:
        data += user.recv(1024)
    msg = data.decode().strip()


# Complete the program
