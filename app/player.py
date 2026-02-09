# This will hold the Player class
class Player:
    def __init__(self, uid, name):
        self.uid = None
        self.name = None

    def __str__(self):
        return "Player ID: ", str(self.uid), " - Name: ", str(self.name)
