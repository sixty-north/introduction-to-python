from itertools import chain, permutations

from .room import Room
from ..direction import Direction


DIR_COMPLEMENTS = {
    from_dir: start_dir
    for from_dir, start_dir
    in chain(permutations((Direction.North, Direction.South)),
             permutations((Direction.East, Direction.West)))
}


def connect(room_from: Room, room_to: Room, dir_from: Direction):
    dir_to = DIR_COMPLEMENTS[dir_from]

    if room_from.doors.get(dir_from) is not None:
        raise ValueError(
            'The {} door in {} is already assigned'.format(
                dir_from.value, room_from))

    if room_to.doors.get(dir_to) is not None:
        raise ValueError(
            'The {} door in {} is already assigned'.format(
                dir_from.value, room_from))

    room_from.doors[dir_from] = room_to
    room_to.doors[dir_to] = room_from


def room_details(room):
    """Get the details of the current room.
    """
    yield room.description
    for direction in sorted(d.value for d in room.doors):
        yield 'There is a door to the {}.'.format(direction)
