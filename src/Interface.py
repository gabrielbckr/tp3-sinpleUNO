
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
        # Mensagem de Recusa
        if cmd == "F":
            self.shouldStop = True
        # Mensagem de texto (T)​
        # Mensagem de jogada (P)​ 
        # Mensagem de jogada inválida (I)​ 
        # Mensagem de perdeu a vez (Y)​ 
        # Mensagem de situação (S)​ 
        # Mensagem de fim de partida (E)​
            