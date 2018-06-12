from .room import Room


class LlamaRoom(Room):
    """This is a subclass of Room which contains some llamas.
    """

    def __init__(self, count):
        super().__init__(
            contents={'llama': count})

    @property
    def description(self):
        return 'This room is filled with {} serene llamas.'.format(
            self.contents['llama'])

    def process_command(self, command, player):
        if command == 'pet llama':
            if self.contents['llama'] < 1:
                return ['Unfortunately there are no llamas to pet.']
            else:
                self.contents['llama'] -= 1
                return ['The llama looks pleased and then gallops off, '
                        'its mission in this dimension completed.']

        return None
