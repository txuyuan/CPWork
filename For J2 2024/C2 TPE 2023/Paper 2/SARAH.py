import socket
my_socket = socket.socket()
my_socket.bind(('127.0.0.1',3036))
my_socket.listen()
user, addr = my_socket.accept()

EOL = b"\n"

# Sarah states the number
initial = int(input("How many nuggets? "))
user.sendall(str(initial).encode())
user.sendall(EOL)

win = True

while True:
    data = b''
    while b'\n' not in data:
        data += user.recv(1024)
    msg = data.decode().strip()
    nuggets = int(msg)

    if nuggets <= 0:
        break

    print(f"There are {nuggets} nuggets left. ")

    success = False 
    while (not success):
        taken = int(input("How many to take? "))
        if (taken >= 1) and (taken <= 3) and (taken <= nuggets):
            success = True
    nuggets -= taken 

    user.sendall(str(nuggets).encode())
    user.sendall(EOL)
    if (nuggets <= 0):
        win = False 
        break

user.close()
my_socket.close()

print("You win. " if win else "You lose. ")


# Complete the program
