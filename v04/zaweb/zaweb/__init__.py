from flask import Flask, request
from flask.json import jsonify
from zorkalike.rooms.util import room_details

from zaweb.processor import Processor


def create_app(test_config=None):
    app = Flask(__name__)

    processor = Processor()


    @app.route('/')
    def home_handler():
        return '''<h1>ZAWeb: A web front-end for Zorkalike!</h1>
        <table>
        <tr><th>action</th><th>URL</th></tr>
        <tr><td>show current description</td><td><pre>/description</pre></td></tr>
        <tr><td>execute command</td><td><pre>/command?cmd=&lt;command text&gt;</pre></td></tr>
        <tr><td>show status</td><td><pre>/status</pre></td></tr>
        <tr><td>reset game</td><td><pre>/reset</pre></td></tr>
        </table>
        '''


    @app.route('/description')
    def description_handler():
        desc = ' '.join(room_details(processor.game.current_room))
        return jsonify({
            'description': desc
        })


    @app.route('/status')
    def status_handler():
        return jsonify({
            'alive': processor.game.player.alive
        })


    @app.route('/command')
    def command_handler():
        cmd = request.args['cmd']
        status, msg = processor.process_command(cmd)
        return jsonify({
            'status': status,
            'message': msg
        })


    @app.route('/reset')
    def reset_handler():
        processor.reset()
        return 'game reset'

    return app
