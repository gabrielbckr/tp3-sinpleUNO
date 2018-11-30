
from Card import Card

class Interface:
    hand = list()
    def __init__(self):
        self.shouldStop = 0 
        self.shouldPost = 0 
        self.answer = 0 
    def addCard(self, c):
        self.hand.append(c)
    def solve(self, cmd):
        print(cmd)
        self.shouldStop = 0 
        self.shouldPost = 0 
        self.answer = 0 
        if cmd == "refuse":
            self.shouldStop = True
    def showHand(self):
        for cs in self.hand:
            print(cs)