from Card import Card 
import socketThread

class Player (socketThread.sockThread):
    def __init__(self, s, id = 0, x = False):
        socketThread.sockThread.__init__(self,s, id, x)
        self.numCards = 0
        self.hand = list()
        self.name = "Ninhum"
    # adds a card to players hand
    def setName(self, nn):
        self.name = nn
    def addCard(self, newCard):
        self.hand.append(newCard)
        self.numCards+=1
    # removes a card, indicated by its position, from players hand and returns it 
    def throwCard(self, ii):
        cc = self.hand[ii]
        del self.hand[ii]
        self.numCards-=1
        return cc
    def hasCard(self, c):
        for ii in range(0,len(self.hand)-1):
            if self.hand[ii].number == c.number and self.hand[ii].color == c.color:
                return ii
        return -1
    def isUNO(self):
        return self.numCards == 1
    def getHand(self):
        string = ""
        for cards in self.hand:
            string+=cards.number+cards.color+" "
        return string