
from Card import Card

class Interface:
    def __init__(self):
        self.shouldStop = 0 
        self.shouldPost = 0 
        self.answer = 0 
    def solve(self, cmd):
        self.shouldStop = 0 
        self.shouldPost = 0 
        self.answer = 0
        cmd.split()[0]
        words = cmd.split()

        # Mensagem de Recusa
        if words[0] == "F":
            print(cmd)
            self.shouldStop = True
        # Mensagem de texto (T)​
        elif words[0] == "T":
            for word in range(1, len(words)):
                print(words[word], end=" ")
            print("")
            #print(cmd)
        # Mensagem de jogada (P)​ 
        # Mensagem de jogada inválida (I)​ 
        # Mensagem de perdeu a vez (Y)​ 
        # Mensagem de situação (S)​ 
        # Mensagem de fim de partida (E)​
            