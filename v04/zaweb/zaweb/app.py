from aiohttp import web
from zorkalike.game import make_game, process_standard_commands
from zorkalike.rooms.util import room_details


class Processor:
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


class Handlers:
    def __init__(self):
        self.processor = Processor()
        self.routes = web.RouteTableDef()

    async def home(self, request):
        return web.Response(text='ZAWeb: A web front-end for Zorkalike!')

    async def description(self, request):
        desc = ' '.join(room_details(self.processor.game.current_room))
        return web.json_response({
            'description': desc
        })

    async def status(self, request):
        return web.json_response({
            'alive': self.processor.game.player.alive
        })

    async def command(self, request):
        cmd = request.query['cmd']
        status, msg = self.processor.process_command(cmd)
        return web.json_response({
            'status': status,
            'message': msg
        })

    async def reset(self, request):
        self.processor.reset()
        raise web.HTTPOk


def main():
    app = web.Application()
    handlers = Handlers()
    app.add_routes([
        web.get('/', handlers.home),
        web.get('/description', handlers.description),
        web.get('/status', handlers.status),
        web.get('/command', handlers.command),
        web.get('/reset', handlers.reset)
    ])
    web.run_app(app)


if __name__ == '__main__':
    main()
