from model.organism import Organism
from pyglet.gl import *
from util.draw import circle
from util.vec import Vec


class Predator(Organism):

    top_speed = 100

    def draw(self):
        glColor3f(0.2, 0.4, 0.5)
        circle(self.p, 10)

    def pathfind(self, prey):
        if prey:
            direction = prey.p - self.p
            self.v = Vec(
                (self.top_speed * direction.x) / direction.abs(),
                (self.top_speed * direction.y) / direction.abs()
            )
        else:
            self.v = Vec(0, 0)
