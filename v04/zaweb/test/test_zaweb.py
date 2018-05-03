from zaweb.app import make_app


async def test_home_page(aiohttp_client, loop):
    app = make_app()
    client = await aiohttp_client(app)
    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert text == 'ZAWeb: A web front-end for Zorkalike!'


async def test_playthrough(aiohttp_client, loop):
    app = make_app()
    client = await aiohttp_client(app)

    resp = await client.get('/description')
    assert resp.status == 200
    data = await resp.json()
    assert data == {'description': 'You are in a dark room. There is a door to the east. There is a door to the north.'}


    resp = await client.get('/command?cmd=south')
    assert resp.status == 200
    data = await resp.json()
    assert data == {
        'status': 'ok',
        'message': 'There is no door to the south. You are in a dark room. There is a door to the east. There is a door to the north.'
    }

    resp = await client.get('/command?cmd=north')
    assert resp.status == 200
    data = await resp.json()
    assert data == {
        'status': 'ok',
        'message': 'This room is filled with 42 serene llamas. There is a door to the south.'
    }

    resp = await client.get('/command?cmd=pet llama')
    assert resp.status == 200
    data = await resp.json()
    assert data == {
        'status': 'ok',
        'message': 'The llama looks pleased and then gallops off, its mission in this dimension completed. This room is filled with 41 serene llamas. There is a door to the south.'
    }

    # response = _process_command('south', game)
    # assert response == []

    # desc = list(room_details(game.current_room))
    # assert desc == ['You are in a dark room.',
    #                 'There is a door to the east.',
    #                 'There is a door to the north.']

    # response = _process_command('east', game)
    # assert response == []

    # desc = list(room_details(game.current_room))
    # assert desc == ['This room contains a grumpy looking bear.',
    #                 'There is a door to the west.']

    # response = _process_command('pet bear', game)
    # assert response == [
    #     'The bear is not impressed and re-enacts "The Revenant" on you.'
    # ]

    # assert not game.player.alive
