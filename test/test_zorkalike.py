try:
    from zorkalike.game import make_game, process_standard_commands
    from zorkalike.rooms.util import room_details
except ImportError:
    from zorkalike import make_game, process_standard_commands, room_details


def _process_command(command, game):
    response = process_standard_commands(command, game)
    if response is None:
        response = game.current_room.process_command(command, game.player)
    return response


def test_playthrough():
    """Just a simple playthrough of the game to help verify different versions.
    """
    game = make_game()
    assert game.player.alive

    desc = list(room_details(game.current_room))
    assert desc == ['You are in a dark room.',
                    'There is a door to the north',
                    'There is a door to the east']

    response = _process_command('south', game)
    assert response == ['There is no door to the south']

    response = _process_command('north', game)
    assert response == []

    desc = list(room_details(game.current_room))
    assert desc == ['This room is filled with 42 serene llamas.', 'There is a door to the south']

    response = _process_command('pet llama', game)
    assert response == [
        'The llama looks pleased and then gallops off, its mission in this dimension completed.',
    ]

    desc = list(room_details(game.current_room))
    assert desc == [
        'This room is filled with 41 serene llamas.',
        'There is a door to the south'
    ]

    response = _process_command('south', game)
    assert response == []

    desc = list(room_details(game.current_room))
    assert desc == ['You are in a dark room.',
                    'There is a door to the north',
                    'There is a door to the east']

    response = _process_command('east', game)
    assert response == []

    desc = list(room_details(game.current_room))
    assert desc == ['This room contains a grumpy looking bear.',
                    'There is a door to the west']

    response = _process_command('pet bear', game)
    assert response == [
        'The bear is not impressed and re-enacts "The Revenant" on you.'
    ]

    assert not game.player.alive
