from zorkalike.player import Player

from .direction import Direction
from .rooms.bear_room import BearRoom
from .rooms.kazoo_room import KazooRoom
from .rooms.llama_room import LlamaRoom
from .rooms.static_room import StaticRoom
from .rooms.util import connect, room_details


class Game:
    def __init__(self, current_room, player):
        self.current_room = current_room
        self.player = player


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


def main():
    main_loop(make_game())
