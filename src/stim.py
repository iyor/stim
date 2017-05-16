import pyglet
from pyglet.gl import *
from math import pi, sin, cos
import draw
from organism import Organism

window = pyglet.window.Window(800, 600)

glClearColor(0.1, 0.2, 0.3, 1)

organisms = [Organism(100, 120), Organism(200, 300)]

@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    for o in organisms:
        draw.predator(o)

def update(dt):
    draw.circle(100,100,100)
    for o in organisms:
        o.update(dt)

pyglet.clock.schedule_interval(update, 1/120.0)

if __name__ == '__main__':
    pyglet.app.run()
