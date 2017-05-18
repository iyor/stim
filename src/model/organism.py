from abc import ABC, abstractmethod
from lib.vec import Vec


class Organism(ABC):

    def __init__(self, x, y):
        self.p = Vec(x, y)
        self.v = Vec(100, 100)

    def update(self, dt):
        self.p += self.v * dt

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def pathfind():
        pass
