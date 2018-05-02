import zorkalike.player
import zorkalike.rooms.util

from .direction import Direction
from .rooms.bear_room import BearRoom
from .rooms.llama_room import LlamaRoom
from .rooms.static_room import StaticRoom
from .rooms.util import connect, print_room_details


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

    connect(start_room, llama_room, Direction.North)
    connect(start_room, bear_room, Direction.East)

    return Game(start_room, zorkalike.player.Player())


def process_standard_commands(command, game):
    """Process commands which are common to all rooms.

    This includes things like following directions, checking inventory, exiting
    the game, etc.

    Returns true if the command is recognized and processed. Otherwise, returns
    false.

    """
    if command in (d.value for d in game.current_room.doors):
        room = game.current_room.doors[Direction(command)]
        game.current_room = room
    elif command in (d.value for d in Direction):
        print('There is no door to the {}'.format(command))
    elif command == 'description':
        print(game.current_room.description)
    elif command == 'inventory':
        print('Inventory %s' % game.player.inventory)
    elif command == 'quit':
        game.player.alive = False
    else:
        # unrecognized command
        return False

    return True


def main_loop(game):
    """Process commands from the user until they die.
    """
    while True:
        if not game.player.alive:
            print('You are dead.')
            return

        print('')
        print_room_details(game.current_room)
        command = input('> ')
        handled = process_standard_commands(command, game) \
            or game.current_room.process_command(command, game.player)
        if not handled:
            print('unrecognized command!')
