from zorkalike.rooms.room import Room


class StartRoom(Room):
    @property
    def description(self):
        return 'You are in a dark room.'
