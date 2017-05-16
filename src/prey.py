from organism import Organism
from pyglet.gl import *
import draw

class Prey(Organism):

    def draw(self):
        glColor3f(0.1, 0.7, 0.5)
        draw.circle(self.x, self.y, 4)

    def pathfind():
        return
