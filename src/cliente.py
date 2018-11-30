import sys
import socket as sock
from Interface import Interface 
from socketThread import sockThread
import threading 

class thInterface (Interface, threading.Thread):
    def __init__(self, s):
        threading.Thread.__init__(self)
        Interface.__init__(self)
        self.s = s
    def run(self):
        return self.solve(self.s)

if (len(sys.argv))<3:
    print ("Uso: python3 servidor.py <host> <porta>")
host = sys.argv[1]
port = int(sys.argv[2])
if host == 'local' or host == 'Local':
    host = '127.0.0.1'

s = sock.socket(sock.AF_INET,sock.SOCK_STREAM,0)
s.connect((host, port))
server = sockThread(s)

while True:
    iT = thInterface(server.get().decode())
    stop, shouldPost, answer = iT.start()
    if stop:
        break
    if shouldPost:
        server.post(answer)


s.close()
