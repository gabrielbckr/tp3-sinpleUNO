import sys
import socket as sock

print (len(sys.argv))
if (len(sys.argv))<3:
    print ("Uso: python3 servidor.py <host> <porta>")
host = sys.argv[1]
port = int(sys.argv[2])
if host == 'local' or host == 'Local':
    host = '127.0.0.1'

s = sock.socket(sock.AF_INET,sock.SOCK_STREAM,0)
s.connect((host, port))
data =  "a b c d "

s.send(str(data).encode())

data = s.recv(1024)
print(data.decode())


s.close()
