from Card import Card 
import socketThread

class Player (socketThread.sockThread):
    def __init__(self, s, id = 0):
        socketThread.sockThread.__init__(self,s, id)
        self.numCards = 0
        self.hand = list()
    # adds a card to players hand
    def setName(self, nn):
        self.name = nn
    def addCard(self, newCard):
        self.hand.append(newCard)
    # removes a card, indicated by its position, from players hand and returns it 
    def throwCard(self, ii):
        cc = self.hand[ii]
        del self.hand[ii]
        self.numCards-=1
        return cc
    def hasValidCard(self, actualCard):
        for cs in self.hand:
            if actualCard.isValid(cs):
                return True
        return False
    def isUNO(self):
        return self.numCards == 1