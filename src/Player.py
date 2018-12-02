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
    def throwCard(self, card):
        idx = self.hasCard(card)
        cc = self.hand[idx]
        del self.hand[idx]
        self.numCards-=1
        return cc
    def hasCard(self, c):
        for cards in self.hand:
            if cards.number == c.number and cards.color == c.color:
                return self.hand.index(cards)
        return -1
    def isUNO(self):
        return self.numCards == 1
    def getHand(self):
        string = ""
        for cards in self.hand:
            string+=cards.number+cards.color+" "
        return string