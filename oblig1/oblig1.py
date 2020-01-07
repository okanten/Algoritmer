
import random
import math

class Queue:

    def __init__(self, list=None):
        self.list = list
        if list is None:
            self.list = []

    def add(self, item):
       self.list.append(item)

    def peek(self):
        # Hvis lista er tom, er køen tom.
        if not self.list:
            return False
        return self.list[0]
    
    def remove(self, item=None):
        if not self.list:
            return 'Køen er tom'
        if item is None:
            item = self.list[0]
        self.list.remove(item)

    def size(self):
        return len(self.list.size)

class Plane:

    def __init(self, name):
       self.name = name


class Airport:

    # Konstruktør med default tidsenheter
    def __init__(self, mean, t=10):
       self.mean = self.get_poisson_random(mean)
       self.t = t
       self.total_planes_handled = 0
       self.total_planes_rejected = 0
       self.total_planes_accepted = 0
       self.total_planes_take_off = 0
       self.total_planes_landed = 0



    def get_poisson_random(self, mean):
       r = random
       L = math.exp(-mean)
       k = 0
       p = 1.0
       while p > L:
           p = p * r.random()
           k = k + 1
       return k - 1


    def initialize(self):
       self.in_traffic = Queue()
       self.on_ground = Queue()
       self.in_traffic.add("lol")
       print(self.in_traffic.peek())

    # Disse to metodene er egentlig helt like. Refaktorer.
    def generate_new_planes_for_landing(self):
       amount = random.randint(0,9)
       for planes in xrange(amount):
           plane = Plane("Plane {}".format(planes))
           if len(self.in_traffic) < 11:
               self.in_traffic.add(plane)
           else:
               print("Køen er full, prøv en annen flyplass")
               self.total_planes_rejected = self.total_planes_rejected + 1
           self.total_planes_handled = self.total_planes_handled + 1
           
    def generate_new_planes_to_take_off(self):
        amount = random.randint(0,9)
        for planes in xrange(amount):
            plane = Plane("Plane {}".format(planes))
            if len(self.on_ground) < 11:
                self.on_ground.add(plane)
            else:
                print("Køen på bakken er full. Du må vente")
                self.total_planes_rejected = self.total_planes_rejected + 1
            self.total_planes_handled = self.total_planes_handled + 1

   



a = Airport(0.6)
a.initialize()


