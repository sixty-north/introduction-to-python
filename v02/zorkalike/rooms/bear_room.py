from zorkalike.rooms.room import Room


class BearRoom(Room):
    """A room containing a bear.
    """

    def __init__(self):
        super().__init__(
            contents={'bear': 1})

    def process_command(self, command, player):
        if command == 'pet bear':
            player.alive = False
            return ['The bear is not impressed and re-enacts '
                    '"The Revenant" on you.']
        return None

    @property
    def description(self):
        return 'This room contains a grumpy looking bear.'
