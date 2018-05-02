from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self,
                 contents=None):
        self.doors = {}
        self.contents = dict(contents) if contents else None

    def process_command(self, command, player):
        """Process room-specific commands.
        """
        return False

    @property
    @abstractmethod
    def description(self):
        pass
