from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self,
                 contents=None):
        self.doors = {}
        self.contents = dict(contents) if contents else {}

    def process_command(self, command, player):
        """Process room-specific commands.

        Returns: An iterable of response string if the room handled the
            command, or None.
        """
        return None

    @property
    @abstractmethod
    def description(self):
        pass
