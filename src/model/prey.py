from model.organism import Organism
from pyglet.gl import *
from util.draw import circle
from util.vec import Vec
import random

class Prey(Organism):

    top_speed = 100

    def draw(self):
        glColor3f(0.1, 0.7, 0.5)
        circle(self.p, 4)

    def pathfind(self, predator):
        t = self.top_speed
        self.v = Vec(random.uniform(-t, t), random.uniform(-t, t))

        """
        # The prey could also try to escape from the closest predator:

        direction = self.p - predator.p
        self.v = Vec(
            (self.top_speed * direction.x) / direction.abs(),
            (self.top_speed * direction.y) / direction.abs()
        )
        """
