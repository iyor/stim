from pyglet.gl import *
from math import pi, sin, cos

def predator(p):
    glColor3f(0.2, 0.4, 0.5)
    circle(p.x, p.y, 10)

def prey(p):
    glColor3f(0.1, 0.7, 0.5)
    circle(p.x, p.y, 4)


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

