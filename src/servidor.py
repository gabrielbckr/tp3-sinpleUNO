import sys
import socket as sock
import threading
import queue
import time

class sockThread (threading.Thread):
    def __init__(self, threadID, name, skt, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.s = skt
      self.rcvQ = q
      self.fstop = False
    def run(self):
        while not self.fstop:
            if not self.rcvQ.empty():
                msg = self.rcvQ.get()
                self.s.send(msg.encode())
    def stop(self):
        self.fstop = True
    def post(self, m):
        self.rcvQ.put(m)

class refuseConnection (threading.Thread):
    def __init__(self, sr):
        threading.Thread.__init__(self)
        self.s = sr
        self.fstop = False
    def run(self):
        while not self.fstop:
            self.s.listen(numPlayers)
            r , rr = s.accept()
            r.send("refuse".encode())
            del(rr)
            r.close()
    def stop(self):
        self.fstop = True

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
    q = queue.Queue(100)
    player = sockThread(ii, "player"+str(ii), cl_sock, q)
    playerThreads.append(player)
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
    playerThreads[ii].post(str(msg))
    ii += 1
    time.sleep(0.05)
    if ii >= len(playerThreads):
        ii = 0