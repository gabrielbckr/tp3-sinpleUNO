import sys
import socket as sock
import threading
import queue

class sockThread (threading.Thread):
   def __init__(self, threadID, name, skt, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.s = skt
      self.rcvQ = q
   def run(self):
        #if not self.rcvQ.empty():
        while True:
            msg = self.rcvQ.get()
            self.s.send(msg.encode())

class refuseConnection (threading.Thread):
    def __init__(self, sr):
        threading.Thread.__init__(self)
        self.s = sr
    def run(self):
        self.s.listen(numPlayers)
        r , rr = s.accept()
        r.send("refuse".encode())
        del(rr)
        r.close()

print (len(sys.argv))
if (len(sys.argv))<2:
    print ("Uso: python3 servidor.py <porta> <numero_de_jogadores>")
port = int(sys.argv[1])
host = '127.0.0.1'
numPlayers = int(sys.argv[2])

s = sock.socket(sock.AF_INET,sock.SOCK_STREAM,0)
playerThreads = list()
playerQueues = list()
s.bind((host, port))
ii = 0

s.listen(numPlayers)

while ii < numPlayers:
    cl_sock, cl_addr = s.accept()
    q = queue.Queue(100)
    player = sockThread(ii, "player"+str(ii), cl_sock, q)
    playerThreads.append(player)
    playerQueues.append(q)
    player.start()
    ii+=1

refuser = refuseConnection(s)
refuser.start()

jj = 0
ii = 0
while True:
    jj += 1
    msg = "test"+str(jj)
    print(msg)
    playerQueues[ii].put(str(msg))
    ii += 1
    if ii >= len(playerQueues):
        ii = 0
    