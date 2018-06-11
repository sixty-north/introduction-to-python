from abc import ABC, abstractmethod
from enum import Enum
from itertools import chain, permutations


class Player:
    def __init__(self):
        self.inventory = {}
        self.alive = True

    def __repr__(self):
        return 'Player(alive={}, inventory={})'.format(
            self.alive, self.inventory)


class Room(ABC):
    def __init__(self,
                 contents=None):
        self.doors = {}
        self.contents = dict(contents) if contents else None

    def process_command(self, command, player):
        """Process room-specific commands.

        Returns: An iterable of response string if the room handled the
            command, or None.
        """
        return None

    @property
    @abstractmethod
    def description(self):
        pass


class StaticRoom(Room):
    """A room with a static description"""

    def __init__(self, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._description = description

    @property
    def description(self):
        return self._description


class KazooRoom(Room):
    def __init__(self):
        super(KazooRoom, self).__init__(
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


class LlamaRoom(Room):
    """This is a subclass of Room which contains some llamas.
    """

    def __init__(self, count):
        super(LlamaRoom, self).__init__(
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


class BearRoom(StaticRoom):
    """A room containing a bear.
    """

    def __init__(self):
        super(BearRoom, self).__init__(
            description='This room contains a grumpy looking bear.',
            contents={'bear': 1})

    def process_command(self, command, player):
        if command == 'pet bear':
            player.alive = False
            return ['The bear is not impressed and re-enacts '
                    '"The Revenant" on you.']
        return None


class Game:
    def __init__(self, current_room, player):
        self.current_room = current_room
        self.player = player


class Direction(Enum):
    North = 'north'
    South = 'south'
    East = 'east'
    West = 'west'


DIR_COMPLEMENTS = {
    from_dir: start_dir
    for from_dir, start_dir
    in chain(permutations((Direction.North, Direction.South)),
             permutations((Direction.East, Direction.West)))
}


def connect(room_from: Room, room_to: Room, dir_from: Direction):
    dir_to = DIR_COMPLEMENTS[dir_from]

    if room_from.doors.get(dir_from) is not None:
        raise ValueError(
            'The {} door in {} is already assigned'.format(
                dir_from.value, room_from))

    if room_to.doors.get(dir_to) is not None:
        raise ValueError(
            'The {} door in {} is already assigned'.format(
                dir_from.value, room_from))

    room_from.doors[dir_from] = room_to
    room_to.doors[dir_to] = room_from


def make_game():
    """Construct a game object.
    """
    start_room = StaticRoom('You are in a dark room.')
    llama_room = LlamaRoom(42)
    bear_room = BearRoom()
    kazoo_room = KazooRoom()

    connect(start_room, llama_room, Direction.North)
    connect(start_room, bear_room, Direction.East)
    connect(start_room, kazoo_room, Direction.West)

    game = Game(start_room, Player())
    return game


def process_standard_commands(command, game):
    """Process commands which are common to all rooms.

    This includes things like following directions, checking inventory, exiting
    the game, etc.

    Returns: An iterable of response strings if the command was processed, or
        None.
    """
    response = []
    if command in (d.value for d in game.current_room.doors):
        room = game.current_room.doors[Direction(command)]
        game.current_room = room
    elif command in (d.value for d in Direction):
        response.append('There is no door to the {}.'.format(command))
    elif command == 'description':
        response.append(game.current_room.description)
    elif command == 'inventory':
        response.append('Inventory {}'.format(game.player.inventory))
    elif command == 'quit':
        game.player.alive = False
    else:
        # unrecognized command
        return None

    return response


def room_details(room):
    """Get the details of the current room.
    """
    yield room.description
    for direction in sorted(d.value for d in room.doors):
        yield 'There is a door to the {}.'.format(direction)


def main_loop(game):
    """Process commands from the user until they die.
    """
    while True:
        if not game.player.alive:
            print('You are dead.')
            return

        print('')
        for line in room_details(game.current_room):
            print(line)

        command = input('> ')

        response = process_standard_commands(command, game)
        if response is None:
            response = game.current_room.process_command(command, game.player)

        if response is None:
            print('unrecognized command!')
        else:
            for line in response:
                print(line)


if __name__ == '__main__':
    main_loop(make_game())
