from itertools import chain
from .predator import Predator
from .organism import Organism
import heapq

class Ecosystem:

    def __init__(self, width, height):
        self.prey_list = []
        self.predator_list = []
        self.width = width
        self.height = height

    def add_prey(self, p):
        self.prey_list.append(p)

    def add_predator(self, p):
        self.predator_list.append(p)

    def get_organisms(self):
        return chain(self.prey_list, self.predator_list)

    def get_prey(self):
        return chain(self.prey_list)

    def get_predators(self):
        return chain(self.predator_list)

    def get_no_of_prey(self):
        return len(self.prey_list)

    def get_no_of_predators(self):
        return len(self.predator_list)

    def draw(self):
        for p in self.get_organisms():
            p.draw()

    def update(self, dt):
        for p in self.get_organisms():
            if isinstance(p, Predator):
                target = self.get_closest_prey(p)
                p.pathfind(target)

            p.update(dt)
            self.checkBounds(p)

    def checkBounds(self, o):
        min_x = 0
        min_y = 0
        max_x = self.width
        max_y = self.height
        if o.p.x < min_x:
            o.p.x = max_x
        elif o.p.x > max_x:
            o.p.x = min_x
        if o.p.y < min_y:
            o.p.y = max_y
        elif o.p.y > max_y:
            o.p.y = min_y

    def get_closest_prey(self, p):
        priority_queue = list(map(lambda q: (Organism.euclidean(p, q), q), self.get_prey()))
        heapq.heapify(priority_queue)
        distance, target = heapq.heappop(priority_queue)
        return target
