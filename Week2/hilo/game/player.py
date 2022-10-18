from game.cards import Cards

class Player:
    """A person who control and play de game at the same time.
    
    The responsability of a Player is to start and finish the game.

    Attributes: 

    """

    def __init__(self):
        """Constructs a player.
        
        Args:
            self (Player): an instance of Player.
        """
     

    def start_game(self):

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.calculatePoints()
            self.do_updates()

    def get_inputs(self):



    def do_updates(self):
        
    def calculatePoints(self):

        # if playerChoise == "H" and card2 > card1:
        #     points = 100
        # elif playerChoise == "H" and card2 <= card1:
        #     points = -75
        # elif playerChoise == "L" and card2 < card1:
        #     points = 100
        # elif playerChoise == "L" and card2 >= card1:
        #     points = -75

        # totalScore += points

        # if totalScore <= 0:
        #     break


    def do_outputs(self):

