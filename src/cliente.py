import sys
import socket as sock
import time

if (len(sys.argv))<3:
    print ("Uso: python3 servidor.py <host> <porta>")
host = sys.argv[1]
port = int(sys.argv[2])
if host == 'local' or host == 'Local':
    host = '127.0.0.1'

s = sock.socket(sock.AF_INET,sock.SOCK_STREAM,0)
s.connect((host, port))

ii = 0
while True:
    data = s.recv(1024)
    print(ii, " ", data.decode())
    ii += 1
    if data.decode() == "refuse":
        break

s.close()
