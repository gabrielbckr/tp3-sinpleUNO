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

#family_info, type_info, res = sock.getaddrinfo(host, port)
#s = sock.socket(family_info, type_info)
#s.connect((host, port))
for res in sock.getaddrinfo(host, port, 0, sock.SOCK_STREAM):
    af, socktype, proto, _, sa = res
    s = sock.socket(af, socktype, proto)
    s.connect(sa)
server = sockThread(s, 0, False)
server.start()


iT = Interface(server)
while True:
    iT.solve(server.get())
    time.sleep(0.05)
    if iT.shouldStop:
        time.sleep(5)
        break
server.stop()