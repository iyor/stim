import pyglet
import sys
from random import randint
from pyglet.gl import *
from model.predator import Predator
from model.prey import Prey

window = pyglet.window.Window(800, 600)

glClearColor(0.1, 0.2, 0.3, 1)

organisms = []


@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    for o in organisms:
        o.draw()


def update(dt):
    for o in organisms:
        o.update(dt)
        checkBounds(o)

def checkBounds(o):
    min_x = 0
    min_y = 0
    max_x = window.width
    max_y = window.height
    if o.p.x < min_x:
        o.p.x = max_x
    elif o.p.x > max_x:
        o.p.x = min_x
    if o.p.y < min_y:
        o.p.y = max_y
    elif o.p.y > max_y:
        o.p.y = min_y


pyglet.clock.schedule_interval(update, 1/120.0)

if __name__ == '__main__':
    # Set up the appropriate number of predator and prey organisms
    no_of_pred = int(sys.argv[1])
    no_of_prey = int(sys.argv[2])
    for i in range(no_of_pred):
        organisms.append(
            Predator(randint(0, window.width), randint(0, window.height))
        )
    for i in range(no_of_prey):
        organisms.append(
            Prey(randint(0, window.width), randint(0, window.height))
        )
    pyglet.app.run()
