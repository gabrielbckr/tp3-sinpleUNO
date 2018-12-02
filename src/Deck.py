from Card import Card as card
import random

class Deck:
    def __init__(self):
        self.numcards = 0
        allColors = ['G' , 'Y' , 'B', 'R']
        allNums = ['0', '1' ,'2' , '3', '4', '5', '6', '7', '8' , '9' , '#']
        self.cards = list()
        for nums in allNums:
            for clrs in allColors:
                newCard = card(nums, clrs)
                self.cards.append(newCard)
                self.numcards+=1
    def shuffle(self):
        random.shuffle(self.cards)
    def get1stCard(self):
        self.numcards-=1
        return self.cards.pop()
    def append(self, c):
        self.cards.append(c)
