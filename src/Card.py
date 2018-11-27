class Card:
    def __init__(self, nn, cc): # cc -> cor || nn -> number 
        if cc != 'G' and cc != 'R' and cc != 'B' and cc != 'Y':
            # dar ruim
            print("so pra n ficar o erro ")
        self.color  = cc
        self.number = str(nn)
    def isYellow(self):
        return self.color == 'Y'
    def isGreen(self):
        return self.color == 'G'
    def isRed(self):
        return self.color == 'R'
    def isBlue(self):
        return self.color == 'Y'
    def isJoker(self):
        return self.number == '#'
    def isValid(self, otherCard):
        return otherCard.number == self.number or otherCard.color == self.color