from organism import Organism
from pyglet.gl import *
import draw


class Predator(Organism):

    def draw(self):
        glColor3f(0.2, 0.4, 0.5)
        draw.circle(self.p, 10)

    def pathfind(self):
        return
