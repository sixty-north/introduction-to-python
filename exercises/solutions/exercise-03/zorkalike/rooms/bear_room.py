from .room import Room


class BearRoom(Room):
    """A room containing a bear.
    """

    def __init__(self):
        super(BearRoom, self).__init__(
            contents={'bear': 1,
                      'demeanor': 'grumpy'})

    @property
    def description(self):
        return 'The room contains a {} looking bear.'.format(
            self.contents['demeanor'])

    def process_command(self, command, player):
        if command == 'pet bear':
            if self.contents['demeanor'] == 'grumpy':
                player.alive = False
                return ['The bear is not impressed and re-enacts '
                        '"The Revenant" on you.']
            else:
                return ['The bear purrs contentedly. Wait...purrs? Is this really a bear?']
        elif command == 'play kazoo':
            if player.inventory.get('kazoo', 0) == 0:
                return ["You don't have a kazoo to play!"]
            self.contents['demeanor'] = 'calm'
            return ['The bear enjoys your serenade and is noticeably calmer.']

        return None
