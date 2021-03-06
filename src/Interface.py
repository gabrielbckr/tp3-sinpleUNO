
from Card import Card

class Interface:
    def __init__(self, s):
        self.shouldStop = False
        self.name = "def"
        self.server = s
        self.shouldStop = False
    def solve(self, cmd):
        words = cmd.split()
        # Mensagem de Recusa
        if   words[0] == "F":
            self.shouldStop = True
            print(cmd)
        # Mensagem de texto (T)​
        elif words[0] == "T":
            for word in range(1, len(words)):
                print(words[word], end=" ")
            print("")
        # Mensagem de jogada (P)​ 
        elif words[0] == "P":
            print("Seu turno de jogar, a carta na mesa é "+words[1])
            print("Sua mão é: ",end="")
            self.printHand(words[2:])
            self.printPlayers(words[2:])
            m = input()
            self.server.post(m)
        # Mensagem de jogada inválida (I)​ 
        elif words[0] == "I":
            print("Jogada inválida, a carta na mesa é "+words[1]+".")
            print("Sua mão é: ",end="")
            self.printHand(words[2:])
            m = input()
            self.server.post(m)
        # Mensagem de perdeu a vez (Y)​ 
        elif words[0] == "Y":
            print("Carta #! Você perdeu a vez!", end=" ")
            print("A carta na mesa é "+words[1]+".")
            print("Sua mão é: ",end="")
            self.printHand(words[2:])
            self.printPlayers(words[2:])
        # Mensagem de situação (S)​ 
        elif words[0] == "S":
            print(words[1]+" jogou a carta "+words[2]+".")
            print("É a vez de "+words[3]+".")
            print("Sua mão é: ",end="")
            self.printHand(words[4:])
            self.printPlayers(words[4:])
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
        del words
    def printHand(self,words):
        ii = 0
        while words[ii] != 'X' :
            print(words[ii], end=" ")
            ii += 1
        print("")
    def printPlayers(self,words):
        ii = 0
        while words[ii] != 'X':
            ii+=1
        ii += 1
        while ii < (len(words)-1):
            print(words[ii]+" tem ", end ="")
            ii+=1
            print(words[ii]+" cartas")
            ii+=1