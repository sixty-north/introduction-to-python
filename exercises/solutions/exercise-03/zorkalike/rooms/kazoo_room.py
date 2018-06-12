from zorkalike.rooms.room import Room


class KazooRoom(Room):
    def __init__(self):
        super().__init__(
            contents={'kazoo': 1})

    @property
    def description(self):
        if self.contents['kazoo'] > 0:
            return 'Except for the kazoo, the room you are in is completely unremarkable.'
        else:
            return 'The room you are in is completely unremarkable.'

    def process_command(self, command, player):
        if command == 'take kazoo':
            if self.contents['kazoo'] > 0:
                player.inventory['kazoo'] = 1
                self.contents['kazoo'] -= 1
                return ['You now have a kazoo!']
            else:
                return ['Kazoo? What kazoo?!']

        return None
