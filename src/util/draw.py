import pyglet.gl as gl
from math import pi, sin, cos


def circle(p, radius):
    iterations = int(2 * radius * pi)
    s = sin(2 * pi / iterations)
    c = cos(2 * pi / iterations)

    dx, dy = radius, 0

    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(p.x, p.y)
    for i in range(iterations + 1):
        gl.glVertex2f(p.x + dx, p.y + dy)
        dx, dy = (dx * c - dy * s), (dy * c + dx * s)

    gl.glEnd()
