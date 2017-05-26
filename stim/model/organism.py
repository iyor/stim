from abc import ABC, abstractmethod
from util.vec import Vec
import random

class Organism(ABC):

    observer = None

    def __init__(self, x, y):
        self.p = Vec(x, y)
        self.v = Vec(0, 0)
        self.age = 0
        self.lifespan = 0
        self.reproduction_chance = 0.0

    def update(self, dt):
        self.p += self.v * dt
        self.age += dt
        if random.random() < self.reproduction_chance:
            self.notify_reproduction()
        if self.age > self.lifespan:
            self.notify_death()

    def set_observer(self, obs):
        self.observer = obs

    def notify_death(self):
        self.observer.notify_death(self)

    def notify_reproduction(self):
        self.observer.notify_reproduction(self)

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def pathfind():
        pass

    @staticmethod
    def euclidean(o1, o2):
        return (o1.p - o2.p).abs()
