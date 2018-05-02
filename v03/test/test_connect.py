from hypothesis import given
import hypothesis.strategies as ST
import pytest

from zorkalike.direction import Direction
from zorkalike.rooms.static_room import StaticRoom
from zorkalike.rooms.util import connect, DIR_COMPLEMENTS



@given(ST.sampled_from(Direction))
def test_room_connections_are_complementary(direction):
    r1 = StaticRoom('Room 1')
    r2 = StaticRoom('Room 2')
    dir_comp = DIR_COMPLEMENTS[direction]

    connect(r1, r2, direction)
    assert r1.doors[direction] is r2
    assert r2.doors[dir_comp] is r1


@given(ST.sampled_from(Direction))
def test_connect_throws_ValueError_if_from_door_is_occupied(direction):
    r1 = StaticRoom('R1')
    r2 = StaticRoom('R2')
    connect(r1, r2, direction)

    r3 = StaticRoom('R3')
    with pytest.raises(ValueError):
        connect(r1, r3, direction)


@given(ST.sampled_from(Direction))
def test_connect_throws_ValueError_if_to_door_is_occupied(direction):
    r1 = StaticRoom('R1')
    r2 = StaticRoom('R2')
    connect(r1, r2, direction)

    r3 = StaticRoom('R3')
    with pytest.raises(ValueError):
        connect(r3, r2, direction)
