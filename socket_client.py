import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9999))


while True:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    s.send(str.encode("Message received", "utf-8"))
