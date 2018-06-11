class Player:
    def __init__(self):
        self.inventory = {}
        self.alive = True

    def __repr__(self):
        return 'Player(alive={}, inventory={})'.format(self.alive,
                                                       self.inventory)
