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

        return ('ok', '\n'.join(response))


processor = Processor()

routes = web.RouteTableDef()


@routes.get('/')
async def home_view(request):
    return web.Response(text='ZAWeb: A web front-end for Zorkalike!')


@routes.get('/description')
async def description_view(request):
    desc = '\n'.join(room_details(processor.game.current_room))
    return web.json_response({
        'description': desc
    })


@routes.get('/status')
async def status_view(request):
    return web.json_response({
        'alive': processor.game.player.alive
    })


@routes.get('/command')
async def command_view(request):
    cmd = request.query['cmd']
    status, msg = processor.process_command(cmd)
    return web.json_response({
        'status': status,
        'message': msg
    })


@routes.get('/reset')
async def reset_view(request):
    processor.reset()
    raise web.HTTPOk


def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


if __name__ == '__main__':
    main()
