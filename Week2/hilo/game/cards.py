import random

class Cards:
    def __init__(self):
        
        self.playerChoise = ""
        self.randomCard = 0
        self.score = 0
        self.totalScore = 0
        self.card1 = 0
        self.card2 = 0

    def getCard(self):
        return random.randint(1, 13)

    def calculatePoints (self):
    
    #Quite points por que no tenia caso usarlo por que solo es una simple suma dentro de tus condiciones
        if self.playerChoise == "H" and self.card2 > self.card1:
            self.totalScore += 100
        elif self.playerChoise == "H" and self.card2 <= self.card1:
            self.totalScore -= 75
        elif self.playerChoise == "L" and self.card2 < self.card1:
            self.totalScore += 100
        elif self.playerChoise == "L" and self.card2 >= self.card1:
            self.totalScore -= 75

        return self.totalScore