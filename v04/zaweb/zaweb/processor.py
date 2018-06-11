from zorkalike.game import make_game, process_standard_commands
from zorkalike.rooms.util import room_details


class Processor:
    """Handle processing of game commands.
    """
    def __init__(self):
        self._game = None
        self.reset()

    @property
    def game(self):
        return self._game

    def reset(self):
        self._game = make_game()

    def process_command(self, command):
        if not self.game.player.alive:
            return ('error', 'Dead players can not run commands!')

        response = process_standard_commands(command, self.game)
        if response is None:
            response = self.game.current_room.process_command(command, self.game.player)

        if response is None:
            return ('error', 'unrecognized command!')

        response.extend(room_details(self.game.current_room))

        if not self.game.player.alive:
            response.append('You are dead.')

        return ('ok', ' '.join(response))
