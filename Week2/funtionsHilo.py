from pickle import TRUE
import random
from tkinter.messagebox import YES

# totalScore = 300
# points = 0


# keepPlaying = True
# while keepPlaying:

#     card1 = int (random.randint(1, 13))
#     card2 = int (random.randint(1, 13))
    
#     print ()
#     print (f"The card is: {card1}")
#     playerChoise = input(f'Higher or Lower? (H/L): ').upper()
#     print (f"Next card was: {card2}")


#     if playerChoise == "H" and card2 > card1:
#         points = 100
#     elif playerChoise == "H" and card2 <= card1:
#         points = -75
#     elif playerChoise == "L" and card2 < card1:
#         points = 100
#     elif playerChoise == "L" and card2 >= card1:
#         points = -75

#     totalScore += points

#     if totalScore <= 0:
#         break

#     print (f"Your score is: {totalScore}")
#     keepPlaying = input (f"Play again? (Yes/No): ").upper()
#     if keepPlaying == "NO":
#         keepPlaying = False

# print ("Game Over")
# print ()



############## Programa con funciones ##############
def main():
    
    keepPlaying = True
    totalScore = 300 #Lo puse fuera por que siempre igualaba a 300 ya que estaba dentro del while 

    while keepPlaying:
        firstCard = getCard()
        secondCard = getCard()
        
        print ()
        print (f"The card is: {firstCard}")
        totalScore = calculatePoints(input("Higher or Lower? (H/L): ").upper(), firstCard, secondCard, totalScore) #Points se va por que no sirve no sea pendeje!!!
        print (f"Next card was: {secondCard}")
        print (f"Your score is {totalScore}")

        if totalScore <= 0 :
            keepPlaying = False

        if totalScore > 0 : # para que pregunte si quiere seguir jugando cuando la puntuación es mayor a cero si no ya no va a preguntar
            keepPlaying = continuePlaying()

    print ("Game Over")
    print ()


def calculatePoints (playerChoise, card1, card2, totalScore):
    
    #Quite points por que no tenia caso usarlo por que solo es una simple suma dentro de tus condiciones
    if playerChoise == "H" and card2 > card1:
        totalScore += 100
    elif playerChoise == "H" and card2 <= card1:
        totalScore -= 75
    elif playerChoise == "L" and card2 < card1:
        totalScore += 100
    elif playerChoise == "L" and card2 >= card1:
        totalScore -= 75

    return totalScore


def getCard ():
    return int(random.randint(1, 13))


def continuePlaying():

    keepPlaying = input (f"Play again? (Yes/No): ").upper()
    if keepPlaying != "YES" and keepPlaying != "Y": #Cambie la condición por que al poner cualquier otra letra o palabra que no fuera yes te dejaba continuar jugando y así solo con el Yes te deja seguir
        return False
    else:
        return True

if __name__ == "__main__":
    main()