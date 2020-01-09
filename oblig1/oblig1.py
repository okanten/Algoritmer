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

    # Overrider len() metoden til Python slik at vi også kan bruke den (i tillegg til size) metoden for vår egen klasse.
    def __len__(self):
        return len(self.list)

    # Overrider metoden som blir brukt i loops. Nå kan vi loope over lista til klassen.
    def __iter__(self):
        return iter(self.list)

class Plane:

    # Konstruktør med default på navn. Genererer "random" navn om den er tom.
    def __init__(self, name=None):
        self.plane_types = ["Boeing 747", "Boeing 737 MAX", "Antonov An-2", "Solar Impulse 1"]
        if name is None:
            plane_type = random.randint(0,3)
            pseudo_identifier = random.randint(0, 100)            
            name = '{} [{}]'.format(self.plane_types[plane_type], pseudo_identifier) 
        self.name = name

    @staticmethod 
    def generate_random_identifiers():
        letters = ''

    def __str__(self):
        return self.name

class Airport:

    # Konstruktør med default tidsenheter
    def __init__(self, mean, t=10):
        self.mean = mean 
        self.t = t
        self.total_planes_handled = 0
        self.total_planes_rejected = 0
        self.total_planes_accepted = 0
        self.total_planes_take_off = 0
        self.total_planes_landed = 0
        print(self.mean)

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
        self.time_step()
        

    def time_step(self):
        for step in range(self.t):
            self.generate_new_planes(self.in_traffic)
            self.generate_new_planes(self.on_ground)
            if self.in_traffic.peek():
                self.in_traffic = self.handle_plane(self.in_traffic, 'landing', 'landet')
                self.total_planes_landed += 1
            elif self.on_ground.peek():
                self.on_ground = self.handle_plane(self.on_ground, 'avgang', 'tok av')
                self.total_planes_take_off += 1
                
    # queue er køen som blir brukt. Pre er før handling, post er etter.
    # Eks: pre = landing, post = landet
    # Fly 1 klar for _landing_
    # Fly 1 _landet_
    def handle_plane(self, queue, pre, post) -> Queue: 
        if queue.peek():
            plane = queue.peek()
            print("Fly {} klar for {}".format(plane, pre))
            queue.remove()
            print("Fly {} {}".format(plane, post))
        return queue

    def generate_new_planes(self, queue):
        amount = self.get_poisson_random(self.mean)
        print("AMOUNT: " + str(amount))
        for planes in range(amount):
            plane = Plane()
            if len(queue) < 11:
                queue.add(plane)
            else:
                print("Køen er full")
                self.total_planes_rejected += 1
            self.total_planes_handled += 1



a = Airport(0.3, 20)
a.initialize()


