from Deck import Deck

class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.players = list()
        self.playerhand = list(list())
        self.EndGame = False
        # self.currentPlayer
        # self.previousPlayer 
        self.deck.shuffle()
        # self.currentCard
    def addPlayer(self, p):
        self.players.append(p)
    def rungame(self):
        self.previousPlayer = self.players[-1]
        self.currentPlayer = self.players[0]
        self.currentCard = self.deck.get1stCard()
        while not self.EndGame:
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
        self.Smessage(self.previousPlayer.name, self.currentPlayer.name, self.currentPlayer)
        # Muda de jogador
    def Pmessage(self, p):
        if type(p) is int:
            p = self.players[p] 
        string = self.currentCard.number+self.currentCard.color+" "+p.getHand()+" "
        for player in self.players:
            if player is not p:
                string+=str(player.name)+" "+str(player.numCards)
        return string
    def Smessage(self, nome1, nome2, p):
        if type(p) is int:
            p = self.players[p] 
        string=nome1+" "+self.currentCard.number+self.currentCard.color+" "+nome2+" "+p.getHand()+" "
        for player in self.players:
            if player is not p:
                string+=str(player.name)+" "+str(player.numCards)
        return "S "+string
    def Imessage(self, p):
        if type(p) is int:
            p = self.players[p] 
        string = self.currentCard+" "+p.getHand()
        return "I "+string
    def Emessage(self, p):
        if type(p) is int:
            p = self.players[p] 
        return "E "+p.name
    def giveCards(self):
        numofcards = 7
        for i in range(numofcards):
            i = i # linha inutil pq o vscode fica enchendo  osaco
            for player in self.players:
                player.addCard(self.deck.get1stCard())