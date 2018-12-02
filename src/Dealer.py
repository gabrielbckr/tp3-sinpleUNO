from Deck import Deck
from Card import Card  
class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.players = list()
        self.EndGame = False
        # self.currentPlayer
        # self.previousPlayer 
        self.deck.shuffle()
        # self.currentCard
    def addPlayer(self, p):
        p.post("O")
        p.setName(p.get())
        self.players.append(p)
    def rungame(self):
        self.giveCards()
        self.previousPlayer = self.players[-1]
        self.currentPlayer = self.players[0]
        self.currentCard = self.deck.get1stCard()
        for player in self.players:
            if  player is not self.currentPlayer: #### DEBUG
                message = self.Smessage(self.previousPlayer.name,
                                        self.currentPlayer.name,
                                        player)
                player.post(message)
        while not self.EndGame:
            self.deck.shuffle()
            self.round()
        for ps in self.players:
            ps.stop()
    def round(self):
        # Avisa de quem é a vez
        message = self.Pmessage(self.currentPlayer)
        self.currentPlayer.post(message)
        # Enquanto a mensagem ta errada 
        while True:
            answer = self.currentPlayer.get()
            answer = answer.split()
            if answer[0] == 'P':
                self.currentPlayer.addCard(self.deck.get1stCard())
                self.previousPlayer = self.currentPlayer
                self.currentPlayer = self.nextPlayer()
                break
            elif len(answer) == 3:
                if answer[0] == 'C':
                    thisC = Card(answer[1],answer[2])
                    if self.valid(self.currentPlayer,thisC):
                        self.deck.append(self.currentCard)
                        self.currentCard = self.currentPlayer.throwCard(thisC)
                        self.previousPlayer = self.currentPlayer
                        self.currentPlayer = self.nextPlayer()
                        break
            message = self.Imessage(self.currentPlayer)
            self.currentPlayer.post(message)
        # Se as casrtas do jogador acabou
        if self.previousPlayer.numCards == 0:
            # jogo acabou
            self.EndGame = True
            for player in self.players:
                player.post(self.Emessage(self.previousPlayer))
            return 
        # SE a Carta enviada é o coringa
        if self.currentCard.isJoker():
            self.currentPlayer.post(self.Ymessage(self.currentPlayer))
            self.currentPlayer = self.nextPlayer() 
        # Envia mensagcem S para todos os outros jogadores
        for player in self.players:
            if  player is not self.currentPlayer: #### DEBUG
                message = self.Smessage(self.previousPlayer.name,
                                        self.currentPlayer.name,
                                        player)
                player.post(message)
    def Pmessage(self, p):
        if type(p) is int:
            p = self.players[p] 
        string = self.currentCard.number+self.currentCard.color+" "+p.getHand()+" "
        string+="X "
        for player in self.players:
            if player is not p:
                string+=str(player.name)+" "+str(player.numCards)+" "
        return "P "+string
    def Smessage(self, nome1, nome2, p):
        if type(p) is int:
            p = self.players[p] 
        string=nome1+" "+self.currentCard.number+self.currentCard.color+" "+nome2+" "+p.getHand()+" "
        string+="X "
        for player in self.players:
            if player is not p:
                string+=str(player.name)+" "+str(player.numCards)+" "
        return "S "+string
    def Imessage(self, p):
        if type(p) is int:
            p = self.players[p] 
        string = self.currentCard.number+self.currentCard.color+" "+p.getHand()
        return "I "+string+"X"
    def Emessage(self, p):
        if type(p) is int:
            p = self.players[p] 
        return "E "+p.name
    def Ymessage(self, p):
        string = self.currentCard.number+self.currentCard.color+" "+p.getHand()+" "
        string+="X "
        for player in self.players:
            if player is not p:
                string+=str(player.name)+" "+str(player.numCards)+ " "
        return "Y " + string
    def giveCards(self):
        numofcards = 2
        for i in range(numofcards):
            i = i # linha inutil pq o vscode fica enchendo  osaco
            for player in self.players:
                player.addCard(self.deck.get1stCard())
    def valid(self, p, card):
        idx = self.currentPlayer.hasCard(card)
        if idx > -1:
            if self.currentCard.isValid(
                    self.currentPlayer.hand[idx]):
                return True
        return False
    def nextPlayer(self):
        idx = self.players.index(self.currentPlayer)
        idx+=1
        idx = idx%len(self.players)
        return self.players[idx]
