import sys
import socket as sock
import threading
from Dealer import Dealer
from Player import Player
import socketThread

print ("This is the Server")
if (len(sys.argv))<2:
    print ("Uso: python3 servidor.py <porta> <numero_de_jogadores>")
port = int(sys.argv[1])
host = '127.0.0.1'
numPlayers = int(sys.argv[2])

s = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
s.bind((host, port))

# Conecta com Players
ii = 0

dealer = Dealer()
if numPlayers > 6:
    numPlayers = 6
s.listen(numPlayers)
while ii < numPlayers:
    cl_sock, cl_addr = s.accept()
    player = Player(cl_sock, ii , True)
    player.start()
    dealer.addPlayer(player)
    ii+=1

refuser = socketThread.refuseConnection(s, "F")
refuser.start()
dealer.rungame()
refuser.stop()
