import socket
import random

EOL = b"\n"

socket = socket.socket()
socket.bind(('127.0.0.1', 6000))
socket.listen()

conn, addr = socket.accept()

charCode = random.randint(ord('A'), ord('Z'))

run = True
while run:
    inputS = conn.recv(1024)
    guess = int(inputS.split(EOL)[0].decode())
    
    status = min(max(charCode - guess, -1), 1) 
    conn.sendall(str(status).encode() + EOL)

    if status == 0:
        run = False
