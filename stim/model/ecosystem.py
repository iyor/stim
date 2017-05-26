from itertools import chain
from .predator import Predator
from .prey import Prey
from .organism import Organism
from random import randint

class Ecosystem:

    def __init__(self, width, height):
        self.prey_list = []
        self.predator_list = []
        self.width = width
        self.height = height

    def add_prey(self):
        p = Prey(randint(0, self.width), randint(0, self.height))
        self.prey_list.append(p)
        p.set_observer(self)

    def add_predator(self):
        p = Predator(randint(0, self.width), randint(0, self.height))
        self.predator_list.append(p)
        p.set_observer(self)

    def notify_death(self, p):
        """
        We're getting ValueError due to trying to delete organisms
        that have already been removed. This problem is currently
        fixed with a hacky passing of the error
        """
        try:
            if isinstance(p, Predator):
                if len(self.predator_list) >= 2:
                    self.predator_list.remove(p)
            elif isinstance(p, Prey):
                if len(self.prey_list) >= 2:
                    self.prey_list.remove(p)
        except ValueError:
            pass

    def notify_reproduction(self, p):
        if isinstance(p, Predator):
            self.add_predator()
        elif isinstance(p, Prey):
            self.add_prey()


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
                target = self.get_nearby_organism(o, self.prey_list)
            # No pathfinding is currently implemented for prey
            # elif isinstance(o, Prey):
            #    target = self.get_nearby_organism(o, self.predator_list)

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
                    if len(self.prey_list) >= 2:
                        self.prey_list.remove(q)
                        p.eat()

    def get_random_organism(self, p, organisms):
        return organisms[randint(0, len(organisms) - 1)]

    def get_nearby_organism(self, p, organisms, closest_only = False):
        smallest_distance = 0
        closest_organism = None

        for o in organisms:
            distance = Organism.euclidean(p, o)
            if (closest_only == False) and (distance < 10):
                return o
            if (closest_organism is None) or (distance < smallest_distance):
                smallest_distance = distance
                closest_organism = o

        return closest_organism
