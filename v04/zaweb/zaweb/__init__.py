from flask import Flask, request
from flask.json import jsonify
from zorkalike.rooms.util import room_details

from zaweb.processor import Processor


def create_app(test_config=None):
    app = Flask(__name__)

    processor = Processor()


    @app.route('/')
    def home_handler():
        return 'ZAWeb: A web front-end for Zorkalike!'


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
