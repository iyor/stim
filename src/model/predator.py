from model.organism import Organism
from pyglet.gl import *
from lib.draw import circle


class Predator(Organism):

    top_speed = 100

    def draw(self):
        glColor3f(0.2, 0.4, 0.5)
        circle(self.p, 10)

    def pathfind(self):
        return
