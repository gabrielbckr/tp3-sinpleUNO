
from Card import Card

class Interface:
    def __init__(self):
        self.shouldStop = 0 
        self.shouldPost = 0 
        self.answer = 0 
    def solve(self, cmd):
        print(cmd)
        self.shouldStop = 0 
        self.shouldPost = 0 
        self.answer = 0 
        if cmd == "refuse":
            self.shouldStop = True