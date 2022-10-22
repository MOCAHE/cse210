from game.cards import Cards

class Player:

    def __init__(self):
        
        self.keepPlaying = True
        self.firstCard = 0
        self.secondCard = 0

    def start_game(self):

        card = Cards()
        card.totalScore = 300

        while self.keepPlaying:
            card.card1 = card.getCard()
            card.card2= card.getCard()
            
            print ()
            print (f"The card is: {card.card1}")
            
            card.playerChoise = input("Higher or Lower? (H/L): ").upper()

            card.totalScore = card.calculatePoints() #Points se va por que no sirve no sea pendeje!!!
            print (f"Next card was: {card.card2}")
            print (f"Your score is {card.totalScore}")

            if card.totalScore <= 0 :
                self.keepPlaying = False

            if card.totalScore > 0 : # para que pregunte si quiere seguir jugando cuando la puntuación es mayor a cero si no ya no va a preguntar
                self.keepPlaying = self.continuePlaying()
        
        print ("Game Over")
        print ()

    

    def continuePlaying(self):

        self.keepPlaying = input (f"Play again? (Yes/No): ").upper()
        if self.keepPlaying != "YES" and self.keepPlaying != "Y": #Cambie la condición por que al poner cualquier otra letra o palabra que no fuera yes te dejaba continuar jugando y así solo con el Yes te deja seguir
            return False
        else:
            return True
