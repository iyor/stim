import pyglet
from pyglet.gl import *
from math import pi, sin, cos

window = pyglet.window.Window(800, 600)

glClearColor(0.2, 0.4, 0.5, 1.0)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0, 0, 0)

    circle(200, 200, 100)

def circle(x, y, radius):
    iterations = int(2*radius*pi)
    s = sin(2*pi / iterations)
    c = cos(2*pi / iterations)

    dx, dy = radius, 0

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(iterations+1):
        glVertex2f(x+dx, y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    glEnd()

if __name__ == '__main__':
    pyglet.app.run()
    circle(30, 30 , 40)
