# I took this course last semester so I saw some solutions shown to us, I can't take all the credit for this work.


def main():

    gameBoard = [1, 2, 3,
                4, 5, 6,
                7, 8, 9]
    
    currentPlayer = "X"
    
    while not (winnerComprobation(gameBoard) or tieComprobation(gameBoard)):
        print ()
        printGameBoard(gameBoard)
        print ()
        switch = logicGame(currentPlayer, gameBoard)
        if switch:
            currentPlayer = switchPlayer (currentPlayer)
    printGameBoard(gameBoard)
    print ("Goog game!")

def printGameBoard (gameBoard):
    print (f' {gameBoard[0]} │ {gameBoard[1]} │ {gameBoard[2]}')
    print ("-----------")
    print (f' {gameBoard[3]} │ {gameBoard[4]} │ {gameBoard[5]}')
    print ("-----------")
    print (f' {gameBoard[6]} │ {gameBoard[7]} │ {gameBoard[8]}')

def winnerComprobation(gameBoard):
    return (gameBoard[0] == gameBoard[1] == gameBoard[2] or
            gameBoard[3] == gameBoard[4] == gameBoard[5] or
            gameBoard[6] == gameBoard[7] == gameBoard[8] or
            gameBoard[0] == gameBoard[3] == gameBoard[6] or
            gameBoard[1] == gameBoard[4] == gameBoard[7] or
            gameBoard[2] == gameBoard[5] == gameBoard[8] or
            gameBoard[0] == gameBoard[4] == gameBoard[8] or
            gameBoard[2] == gameBoard[4] == gameBoard[6])

def tieComprobation (gameBoard):
    for box in range(9):
        if gameBoard[box] != "X" and gameBoard[box] != "O":
            return False
    return True 

def switchPlayer (currentPlayer):
    if currentPlayer == "X":
        return "O"
    else:
        return"X"

def logicGame(currentPlayer, gameBoard):
    box = int(input(f"{currentPlayer}'s turn to choose a box (1-9): "))
    if gameBoard[box - 1] == 'X' or gameBoard[box - 1] == 'O':
        print (f"The box {box} is taken, choose another one")
        return False
    else:
        gameBoard[box - 1] = currentPlayer
        return True

main()

