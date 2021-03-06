from model.organism import Organism
from pyglet.gl import *
from util.draw import circle
from util.vec import Vec


class Predator(Organism):

    top_speed = 100
    max_lifespan = 100
    lifespan_increase = 0.4
    reproduction_increase = 0.0005
    increase_limit = 3

    def __init__(self, x, y):
        super(Predator, self).__init__(x, y)
        self.lifespan = 3
        self.reproduction_chance = 0.003

    def draw(self):
        glColor3f(0.2, 0.4, 0.5)
        circle(self.p, 10)

    def pathfind(self, prey):
        if prey:
            direction = prey.p - self.p
            absolute = direction.abs()

            if absolute != 0:
                self.v = Vec(
                    (self.top_speed * direction.x) / absolute,
                    (self.top_speed * direction.y) / absolute
                )
            else:
                self.v = Vec(0, 0)
        else:
            self.v = Vec(0, 0)

    def eat(self):
        if (self.age - self.lifespan < self.increase_limit and
            self.lifespan < self.max_lifespan):
            self.lifespan += self.lifespan_increase
            self.reproduction_chance += self.reproduction_increase
