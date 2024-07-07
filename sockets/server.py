import socket

try:
    with socket.socket() as s:
        s.bind(('127.0.0.1', 12345))
        s.listen()

        while True:
            conn, addr = s.accept()
            print("Connection by " + str(addr))


            conn.sendall(b"Hello mum from server \r\n")
            conn.close()

        s.close()

except KeyboardInterrupt:
    print("Quitting")
finally:
    print("Done.")

s = socket.socket()
