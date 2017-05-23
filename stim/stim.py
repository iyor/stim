import pyglet
import sys
from itertools import chain
from pyglet.gl import *
from util.output import output_data, remove_data
from model.predator import Predator
from model.ecosystem import Ecosystem
from model.prey import Prey

width = 1000
height = 700

EXPORT_DATA_RATE = 3

window = pyglet.window.Window(width, height)

glClearColor(0.1, 0.2, 0.3, 1)

eco = Ecosystem(width, height)

@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    eco.draw()

# Update model state
def update(dt):
    eco.update(dt)

# Write model state to file
def export_data(dt):
    output_data(eco)

# Set simulation update schedule interval
pyglet.clock.schedule_interval(update, 1/120.0)

# Set data export interval time
pyglet.clock.schedule_interval(export_data, EXPORT_DATA_RATE)

if __name__ == '__main__':

    # Reset output file
    remove_data()

    # Set up the appropriate number of predator and prey organisms
    no_of_pred = int(sys.argv[1])
    no_of_prey = int(sys.argv[2])
    for i in range(no_of_pred):
        eco.add_predator()
    for i in range(no_of_prey):
        eco.add_prey()
    pyglet.app.run()
