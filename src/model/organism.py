from abc import ABC, abstractmethod
from util.vec import Vec


class Organism(ABC):

    def __init__(self, x, y):
        self.p = Vec(x, y)
        self.v = Vec(0, 0)

    def update(self, dt):
        self.p += self.v * dt

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def pathfind():
        pass

    @staticmethod
    def euclidean(o1, o2):
        return (o1.p - o2.p).abs()
