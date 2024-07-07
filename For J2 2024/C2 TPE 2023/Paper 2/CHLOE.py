import socket 

EOL = b"\n"

user = socket.socket()
user.connect(("127.0.0.1", 3036))

nuggets = 0 
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

print("You win. " if win else "You lose. ")
