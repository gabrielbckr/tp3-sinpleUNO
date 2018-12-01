import sys
import socket as sock
import threading
import time
from Dealer import Dealer
from Player import Player
import socketThread

print ("This is the Server")
if (len(sys.argv))<2:
    print ("Uso: python3 servidor.py <porta> <numero_de_jogadores>")
port = int(sys.argv[1])
host = '127.0.0.1'
numPlayers = int(sys.argv[2])

s = sock.socket(sock.AF_INET,sock.SOCK_STREAM,0)
s.bind((host, port))

# Conecta com Players
ii = 0

dealer = Dealer()
s.listen(numPlayers)
while ii < numPlayers:
    cl_sock, cl_addr = s.accept()
    player = Player(cl_sock, ii , True)
    player.start()
    dealer.addPlayer(player)
    ii+=1

refuser = socketThread.refuseConnection(s, "F")
refuser.start()

jj = 0
ii = 0
dealer.giveCards()
dealer.previousPlayer = dealer.players[-1]
dealer.currentPlayer = dealer.players[0]
dealer.currentCard = dealer.deck.get1stCard()
while True:
    jj += 1
    msg = "T this is my test test"
    dealer.players[ii].post(dealer.Ymessage(dealer.players[ii]))
    ii += 1
    time.sleep(0.05)
    if ii >= len(dealer.players):
        ii = 0