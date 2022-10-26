from game.wordsLogic import Words
from game.parachute import Parachute

class Player:

    def __init__ (self):
        self._parachute = Parachute()
        self._wordsLogic = Words()
        self._choicePlayer = ""
        self._endGame = False
        self._keepPlaying = True


    def startGame(self):
        while self._keepPlaying:
            self._printOutputs()

            if not self._endGame:
                self._getInputs()
                self._doUpdates()

        if self._endGame:
            print()
            print("GAME OVER")
            print()

    
    def _getInputs (self):
        print()
        self._choicePlayer = input("Guess a letter [a-z]: ").lower()
        print()

    def _doUpdates (self):
        wordCorrect = self._wordsLogic.logicWord(self._choicePlayer)
        if not wordCorrect:

            if self._parachute.headParachute():
                self._keepPlaying = False
                self._parachute.changeHeadParachute()
                self._parachute.printParachute()
                self._endGame = True
            else:
                self._parachute.eraseParachute()
        else:
            self._keepPlaying == False

    
    def _printOutputs (self):
        print()
        self._wordsLogic.printWord()
        self._parachute.printParachute()
        lword = ""
        for letter in self._wordsLogic.choiceWord:
            lword += letter.strip()

        if self._wordsLogic.word == lword:
            self._endGame = True
            self._keepPlaying = False


