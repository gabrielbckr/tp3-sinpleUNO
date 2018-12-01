
from Card import Card

class Interface:
    def __init__(self,shouldStop, s):
        self.shouldStop = shouldStop
        self.name = "def"
        self.server = s
        self.shouldStop = False
    def solve(self, cmd):
        words = cmd.split()
        # Mensagem de Recusa
        if words[0] == "F":
            self.shouldStop = True
            print(cmd)
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
        elif words[0] == "E":
            self.shouldStop = True
            if words[1] == self.name:
                print("Voce venceu a partida!")
            else:
                print(words[1]+" Venceu a partida!")
        # Mensagem de inicio de partida (O) para enviar o nome do jogador
        elif words[0] == "O":
            self.name = input("Entrando na partida, insira o nome do jogador:\n")
            self.server.post(self.name)