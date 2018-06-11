def test_home_page(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.data == b'ZAWeb: A web front-end for Zorkalike!'


def test_playthrough(client):
    resp = client.get('/description')
    assert resp.status_code == 200
    assert resp.json == {'description': 'You are in a dark room. There is a door to the east. There is a door to the north.'}


    resp = client.get('/command?cmd=south')
    assert resp.status_code == 200
    assert resp.json == {
        'status': 'ok',
        'message': 'There is no door to the south. You are in a dark room. There is a door to the east. There is a door to the north.'
    }

    resp = client.get('/command?cmd=north')
    assert resp.status_code == 200
    assert resp.json == {
        'status': 'ok',
        'message': 'This room is filled with 42 serene llamas. There is a door to the south.'
    }

    resp = client.get('/command?cmd=pet llama')
    assert resp.status_code == 200
    assert resp.json == {
        'status': 'ok',
        'message': 'The llama looks pleased and then gallops off, its mission in this dimension completed. This room is filled with 41 serene llamas. There is a door to the south.'
    }
