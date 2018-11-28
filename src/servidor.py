import sys
import socket as sock
import threading
import time

class sockThread (threading.Thread):
   def __init__(self, threadID, name, skt):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.s = skt
   def run(self):
       self.s.send("Toma a resposta porra".encode())
       return True


print (len(sys.argv))
if (len(sys.argv))<2:
    print ("Uso: python3 servidor.py <porta> <numero_de_jogadores>")
port = int(sys.argv[1])
host = '127.0.0.1'
numPlayers = int(sys.argv[2])


s = sock.socket(sock.AF_INET,sock.SOCK_STREAM,0)
playerThreads = list()
s.bind((host, port))
ii = 0
s.listen(numPlayers)
while ii < numPlayers:
    cl_sock, cl_addr = s.accept()
    player = sockThread(ii, "player"+str(ii), cl_sock)
    playerThreads.append(player)
    data = cl_sock.recv(1024)
    print(data.decode())   # Encoding e decoding was necessary in python3 but not python2
    player.start()
    player.join()
    ii+=1



pos = list(data)
