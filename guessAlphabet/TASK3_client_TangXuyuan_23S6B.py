import socket

EOL = b"\n"

socket = socket.socket()
socket.connect(('127.0.0.1', 6000))

# Get user input, send to server, display output. Quit when guessed correctly

run = True
while run:
    guess = ord(input("Enter character guess: "))
    socket.sendall(str(guess).encode() + EOL)
    response = socket.recv(1024)
   
    status = int(response.split(EOL)[0].decode())
    
    if status == 0:
        print("Correct! Good job")
        run = False
    elif status == -1:
        print("The answer is before your guess")
    elif status == 1:
        print("The answer is after your guess")
    
