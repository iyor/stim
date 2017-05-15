import pyglet
from pyglet.gl import *
from math import pi, sin, cos
import draw

window = pyglet.window.Window(800, 600)

glClearColor(0.2, 0.4, 0.5, 1.0)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0, 0, 0)

    draw.circle(200, 200, 100)

if __name__ == '__main__':
    pyglet.app.run()
