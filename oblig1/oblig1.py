import random
import math

class Queue:
    """
        En array-basert queue implementasjon. Læreboka anbefaler en annen implementasjon, men jeg så ingen grunn til å skrive noe annet enn det her for dette formålet.
    """ 
    def __init__(self, capacity=256, list=None):
        self.list = list
        self.capacity = capacity
        if list is None:
            self.list = []

    # Legger til en sjekk i add for å forsikre oss om at det ikke er mulig å legge til flere elementer om køen er full. Denne er strengt tatt ikke nødvendig i dette tilfellet, siden vi sjekker lengre ned, men future-proofing.
    def add(self, item):
        if len(self.list) < self.capacity:            
            self.list.append(item)
        else:
            return False

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

    def get_capacity(self):
        return int(self.capacity)

    def size(self):
        return len(self.list.size)

    # Overrider len() metoden til Python slik at vi også kan bruke den (i tillegg til size) metoden for vår egen klasse.
    def __len__(self):
        return len(self.list)

    # Overrider metoden som blir brukt i loops. Nå kan vi loope over lista til klassen.
    def __iter__(self):
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
        self.in_traffic = Queue(20)
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
                
    # queue er køen som blir brukt. Pre er før handling, post er etter.
    # Eks: pre = landing, post = landet
    # Fly 1 klar for _landing_
    # Fly 1 _landet_
    def handle_plane(self, queue, pre, post): 
        if queue.peek():
            plane = queue.peek()
            print("Fly {} klar for {}".format(plane, pre))
            queue.remove()
            print("Fly {} {}".format(plane, post))

    def generate_new_planes(self, queue):
        amount_of_new_planes = self.get_poisson_random(self.mean)
        for planes in range(amount_of_new_planes):
            plane = Plane()
            if len(queue) < queue.get_capacity():
                queue.add(plane)
            else:
                print("Køen er full")
                self.total_planes_rejected += 1
            self.total_planes_handled += 1



a = Airport(0.3, 20)
a.initialize()


