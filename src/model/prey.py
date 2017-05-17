from model.organism import Organism
from pyglet.gl import *
from lib.draw import circle


class Prey(Organism):

    def draw(self):
        glColor3f(0.1, 0.7, 0.5)
        circle(self.p, 4)

    def pathfind():
        return
