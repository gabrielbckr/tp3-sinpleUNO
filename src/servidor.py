import sys
import socket as sock
import threading
import time
import socketThread


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
    player = socketThread.sockThread(cl_sock, ii, "player"+str(ii))
    playerThreads.append(player)
    player.start()
    ii+=1

refuser = socketThread.refuseConnection(s)
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