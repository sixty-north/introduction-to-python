from .static_room import StaticRoom

class BearRoom(StaticRoom):
    """A room containing a bear.
    """

    def __init__(self):
        super(BearRoom, self).__init__(
            description='This rooms contains a grumpy looking bear.',
            contents={'bear': 1})

    def process_command(self, command, player):
        if command == 'pet bear':
            player.alive = False
            return ['The bear is not impressed and re-enacts "The Revenant" on you.']
        return None
