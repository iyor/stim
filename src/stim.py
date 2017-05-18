import pyglet
import sys
from itertools import chain
from random import randint
from pyglet.gl import *
from model.predator import Predator
from model.ecosystem import Ecosystem
from model.prey import Prey

width = 800
height = 600

window = pyglet.window.Window(width, height)

glClearColor(0.1, 0.2, 0.3, 1)

eco = Ecosystem(width, height)

@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    eco.draw()

def update(dt):
    eco.update(dt)

pyglet.clock.schedule_interval(update, 1/120.0)

if __name__ == '__main__':
    # Set up the appropriate number of predator and prey organisms
    no_of_pred = int(sys.argv[1])
    no_of_prey = int(sys.argv[2])
    for i in range(no_of_pred):
        eco.add_predator(
            Predator(randint(0, window.width), randint(0, window.height))
        )
    for i in range(no_of_prey):
        eco.add_prey(
            Prey(randint(0, window.width), randint(0, window.height))
        )
    pyglet.app.run()
