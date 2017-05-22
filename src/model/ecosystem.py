from itertools import chain
from .predator import Predator
from .prey import Prey
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

    def get_no_of_prey(self):
        return len(self.prey_list)

    def get_no_of_predators(self):
        return len(self.predator_list)

    def draw(self):
        for p in self.get_organisms():
            p.draw()

    def update(self, dt):
        for o in self.get_organisms():
            target = None
            if isinstance(o, Predator):
                target = self.get_closest_organism(o, self.prey_list)
            elif isinstance(o, Prey):
                target = self.get_closest_organism(o, self.predator_list)

            o.pathfind(target)
            o.update(dt)
            self.checkBounds(o)

        self.checkCollisions()

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

    def checkCollisions(self):
        for p in self.predator_list:
            for q in self.prey_list:
                if (p.p - q.p).abs() < 1:
                    self.prey_list.remove(q)


    def get_closest_organism(self, p, organisms):
        priority_queue = list(map(lambda o: (Organism.euclidean(p, o), o), organisms))
        heapq.heapify(priority_queue)
        if len(priority_queue) > 0:
            distance, target = heapq.heappop(priority_queue)
            return target
        return None
