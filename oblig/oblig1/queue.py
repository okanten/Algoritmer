import random
import math

class Queue:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.list = []
        # Må fylle listen med noe for å kunne bruke list[index].
        for x in range(capacity):
            self.list.append(x)
        self.count = 0
        self.rear = -1 
        self.front = -1 
 
    def enqueue(self, element):
        # Start condition.
        if (self.is_queue_empty()):
            print("Queue Empty")
            self.rear = 0 
            self.front = 0
            self.list[self.rear] = element
            self.rear += 1
            self.count += 1
            print("Added to queue")
        elif ( ((self.rear + 1) % self.size()) == self.front):
            for plane in self.list:
                print("###")
                print(plane)
                print("###\n")
            print("Queue is full")
        else:
            self.rear += (1) % self.size() 
            self.list[self.rear] = element
            self.count += 1
            print("Added to queue")

    def dequeue(self):
        if (self.is_queue_empty()):
            return ("Queue is empty")
        elif (self.front == self.rear):
            self.rear = -1
            self.front = -1
            self.count = 0
        else:
            self.front = (self.front + 1) % self.size()
            if self.count > 0:
                self.count -= 1 
            return ("Removed {} from the queue".format(self.list[self.front]))
 
    def peek(self):
        if not self.is_queue_empty():
            return self.list[self.front]
        return False

    def is_queue_empty(self):
        return (self.rear == -1 and self.front == -1)
        
    def is_queue_full(self):
        return ( ((self.rear + 1) % self.size()) == self.front)

    def size(self):
        return self.capacity

    # Overrider len() metoden til Python slik at vi kan se hvor mange elementer er i kø.
    def __len__(self):
        return self.count
        """
        count = 0
        tmp_front = self.front
        tmp_rear = self.rear
        # Finne differansen mellom front og rear
        while (tmp_front != tmp_rear):
           tmp_front = (tmp_front + 1) % self.size()
           count += 1
        return count 
        """

    # Overrider metoden som blir brukt i loops. Nå kan vi loope (iterere) over lista til klassen
    def __iter__(self):
        return False
        return iter(self.list)


class Plane:
    """
        Klasse som egentlig bare skal holde på informasjon om fly.
        Genererer navn selv om ingenting blir spesifisert. Har pseudo-unique identifier.
    """

    def __init__(self, name=None):
        self.plane_types = ["Boeing 747", "Boeing 737 MAX", "Antonov An-2", "Solar Impulse 1"]
        if name is None:
            plane_type = random.randint(0,3)
            pseudo_identifier = random.randint(0, 100)
            name = '{} [{}]'.format(self.plane_types[plane_type], pseudo_identifier)
        self.name = name

    # Overrider str så vi får navnet på flyet istedenfor en objekt-referanse når vi bruker print på et plane-objekt.
    def __str__(self):
        return self.name


class Airport:

    """
        Klasse som simulerer handlingene til en flyplass, er også den som simulerer algoritmen.
    """


    # Konstruktør med default tidsenheter
    def __init__(self, mean, time_laps=10):
        self.mean = mean 
        self.time_laps = time_laps 
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

    # Initialiserer kjøringen av algoritmen. Oppretter kø-objekter og starter simuleringen.
    def initialize(self):
        self.in_traffic = Queue(5)
        self.on_ground = Queue(20)
        self.time_step() 

    def time_step(self):
        for step in range(self.time_laps):
            self.generate_new_planes(self.in_traffic)
            self.generate_new_planes(self.on_ground)
            # Prioriterer flyene i luften slik oppgaven ber om
            if self.in_traffic.peek():
               # self.in_traffic = 
                self.handle_plane(self.in_traffic, 'landing', 'landet')
                self.total_planes_landed += 1
            elif self.on_ground.peek():
               # self.on_ground = 
                self.handle_plane(self.on_ground, 'avgang', 'tok av')
                self.total_planes_take_off += 1
        print(self.total_planes_accepted)
                
    # queue er køen som blir brukt. Pre er før handling, post er etter.
    # Eks: pre = landing, post = landet
    # Fly 1 klar for _landing_
    # Fly 1 _landet_
    def handle_plane(self, queue, pre, post): 
        if queue.peek():
            plane = queue.peek()
            print("Fly {} klar for {}".format(plane, pre))
            queue.dequeue()
            print("Fly {} {}".format(plane, post))

    def generate_new_planes(self, queue):
        amount_of_new_planes = self.get_poisson_random(self.mean)
        for planes in range(amount_of_new_planes):
            plane = Plane()
            if not queue.is_queue_full():
                queue.enqueue(plane)
            else:
                print("Køen er full")
                self.total_planes_rejected += 1
            self.total_planes_handled += 1


queue = Queue(5)
queue.enqueue(0)
queue.enqueue("DURR")
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue("HURR")
queue.enqueue("HURR")
queue.enqueue("HURR")
queue.enqueue("HURR")
queue.enqueue("HURR")
queue.enqueue("HURR")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

#a = Airport(0.3, 20000)
#a.initialize()


