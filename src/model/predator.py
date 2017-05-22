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
        direction = prey.p - self.p
        self.v = Vec(100 * direction.x / direction.abs(), 100 * direction.y / direction.abs())
        return
