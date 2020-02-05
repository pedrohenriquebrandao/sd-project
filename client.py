import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1238))

msg = s.recv(1024)
print(msg.decode("utf-8"))
s.close()


