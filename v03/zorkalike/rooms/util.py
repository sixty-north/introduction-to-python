from itertools import chain, permutations

from .room import Room
from ..direction import Direction


DIRECTIONS = {
    from_dir: start_dir
    for from_dir, start_dir
    in chain(permutations((Direction.North, Direction.South)),
             permutations((Direction.East, Direction.West)))
}


def connect(room_from: Room, room_to: Room, dir_from: Direction):
    dir_to = DIRECTIONS[dir_from]

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


def print_room_details(room):
    """Print the details of the current room.
    """
    print(room.description)
    for direction in room.doors:
        print('There is a door to the {}'.format(direction.value))
