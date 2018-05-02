from .room import Room


class StaticRoom(Room):
    """A room with a static description"""

    def __init__(self, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._description = description

    @property
    def description(self):
        return self._description
