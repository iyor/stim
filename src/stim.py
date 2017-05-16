import pyglet
import sys
from pyglet.gl import *
from predator import Predator
from prey import Prey

window = pyglet.window.Window(800, 600)

glClearColor(0.1, 0.2, 0.3, 1)

organisms = [Predator(100, 120), Prey(200, 300)]

@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    for o in organisms:
        o.draw()

def update(dt):
    for o in organisms:
        o.update(dt)

pyglet.clock.schedule_interval(update, 1/120.0)

if __name__ == '__main__':
    no_of_pred = sys.argv[1]
    no_of_prey = sys.argv[2]
    print(no_of_pred)
    print(no_of_pred)
    pyglet.app.run()
