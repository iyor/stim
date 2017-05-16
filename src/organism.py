from abc import ABC, abstractmethod


class Organism(ABC):

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.v_x, self.v_y = 100.0, 100.0

    def update(self, dt):
        self.x += self.v_x * dt
        self.y += self.v_y * dt

    @abstractmethod
    def draw(self):
        pass
