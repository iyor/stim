from abc import ABC, abstractmethod
from util.vec import Vec


class Organism(ABC):

    observer = None

    def __init__(self, x, y):
        self.p = Vec(x, y)
        self.v = Vec(0, 0)
        self.age = 0
        self.lifespan = 0
        self.reproduction_interval = 0
        self.time_since_last_reproduction = 0.0

    """
    Sometimes we place an organism in a priority queue to find the closest one.
    If two organisms have the same distance to another, the built-in heapify function
    compares on object instead. In this case we don't care which one to choose,
    and so we simply return the first one.
    """
    def __lt__(self, other):
        return -1

    def update(self, dt):
        self.p += self.v * dt
        self.age += dt
        self.time_since_last_reproduction += dt
        if self.time_since_last_reproduction > self.reproduction_interval:
            self.notify_reproduction()
            self.time_since_last_reproduction = 0.0
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
