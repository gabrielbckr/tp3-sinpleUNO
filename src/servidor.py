import sys
import socket as sock

print (len(sys.argv))
if (len(sys.argv))<3:
    print ("USAGE: python3 servidor.py host port")
host = sys.argv[1]
port = int(sys.argv[2])
if host == 'local' or host == 'Local':
    host = '127.0.0.1'


s = sock.socket(sock.AF_INET,sock.SOCK_STREAM,0)
s.bind((host, port))
s.listen(1)
cl_sock, cl_addr = s.accept()
data = cl_sock.recv(1024)
print(data.decode())   # Encoding e decoding was necessary in python3 but not python2
cl_sock.send(" toam a resposta porra".encode())

pos = list(data)
