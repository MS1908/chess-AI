from abc import ABC, abstractmethod


class GenericPlayer(ABC):
    def __init__(self, player: bool, solver: str = None):
        self.player = player
        self.solver = solver

    @abstractmethod
    def move(self):
        pass
