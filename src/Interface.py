
from Card import Card

class Interface:
    hand = list()
    def __init__(self):
        print("Hello")
    def addCard(self, c):
        self.hand.append(c)
    def solve(self, cmd):
        print(cmd)
    def showHand(self):
        for cs in self.hand:
            print(cs)