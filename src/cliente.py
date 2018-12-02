import sys
import socket as sock
from Interface import Interface 
from socketThread import sockThread
import threading 
import time

if (len(sys.argv))<3:
    print ("Uso: python3 servidor.py <host> <porta>")
host = sys.argv[1]
port = int(sys.argv[2])
if host == 'local' or host == 'Local':
    host = '127.0.0.1'

s = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
s.connect((host, port))
server = sockThread(s, 0, False)
server.start()
shouldStop = False

iT = Interface(server)
while True:
    iT.solve(server.get())
    time.sleep(0.05)
    if iT.shouldStop:
        time.sleep(5)
        break
server.stop()