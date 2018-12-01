import sys
import socket as sock
from Interface import Interface 
from socketThread import sockThread
import threading 
import time

class thInterface (Interface, threading.Thread):
    def __init__(self, s,shouldStop,  sr):
        threading.Thread.__init__(self)
        Interface.__init__(self, shouldStop, sr)
        self.m = s
    def run(self):
        self.solve(self.m)

if (len(sys.argv))<3:
    print ("Uso: python3 servidor.py <host> <porta>")
host = sys.argv[1]
port = int(sys.argv[2])
if host == 'local' or host == 'Local':
    host = '127.0.0.1'

s = sock.socket(sock.AF_INET,sock.SOCK_STREAM,0)
s.connect((host, port))
server = sockThread(s, 0, False)
server.start()
shouldStop = False

while True:
    iT = thInterface(server.get(), shouldStop, server)
    iT.start()
    time.sleep(0.05)
