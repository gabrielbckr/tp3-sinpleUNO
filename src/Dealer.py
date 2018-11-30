from Deck import Deck

class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.players = list()
        self.playerhand = list(list())
        self.EndGame = False
        self.currentPlayer = 0
    def addPlayer(self, p):
        self.players.append(p)
    def rungame(self):
        while self.EndGame:
            self.round()
    def round(self):
        # Avisa de quem é a vez
        message = self.Pmessage(self.currentPlayer)
        self.players[self.currentPlayer].post(message)
        # Enquanto a mensagem ta errada 
        message = self.Imessage(self.currentPlayer)
        self.players[self.currentPlayer].post(message)
        # Checa estado do Jogo
        # Envia mensagem S para todos os outros jogadores
        self.Smessage(self.currentPlayer)
        # Muda de jogador
    def Pmessage(self, p):
        print("")
    def Smessage(self, p):
        print("")
    def Imessage(self, p):
        print("")