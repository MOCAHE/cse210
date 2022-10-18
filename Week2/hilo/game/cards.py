import random

class Cards:
    def __init__(self):
        
        self.playerChoice = 0
        self.randomCard = 0
        self.score = 0

    def getCard(self):
        self.randomCard = random.randint(1, 13)