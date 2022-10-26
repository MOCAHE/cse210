import random

class Words:
    def __init__(self):
        self._words = ["python", "java", "javascript", "code", "core", "linux", "windows"]
        self.word = self.selectWord()
        self.choiceWord = ["_"] * len(self.word)
        self.playerWord = ""


    def selectWord(self):
        return random.choice(self._words)


    def printWord(self):
        for letter in self.choiceWord:
            print (f" {letter} ", end="")
        print("")


    def logicWord(self, choiceWord):
        wordCorrect = False

        for index, character in enumerate(self.word):
            if character == choiceWord:
                self.choiceWord[index] = choiceWord
                wordCorrect = True
        return wordCorrect
        


