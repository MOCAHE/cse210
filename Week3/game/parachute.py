class Parachute:

    def __init__(self):
    #Dibujar Parachute
        self.parachute = [" ", 
    "                      ___ ", 
    "                     /___\ ", 
    "                     \   / ", 
    "                      \ /  ", 
    "                       0  ", 
    "                      /|\   ", 
    "                      / \  ",  
    " ", 
    "                    ^^^^^^^"]
    
    def printParachute(self):
        for line in self.parachute:
            print (line)

    def eraseParachute(self):
        self.parachute.pop(1)

    def headParachute(self):
        return len(self.parachute) == 6

    def changeHeadParachute(self):
        self.parachute[1] = "                       X  "