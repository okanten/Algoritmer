import random
import math

class CircularQueue:
    """
        https://www.pythoncentral.io/circular-queue/
        Oppgaven linker til ferdiglagde klasser i Java, så håper det er greit å bruke ferdiglagde klasser uavhengig av språk.
    """
    #Constructor
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 8

    #Adding elements to the queue
    def enqueue(self,data):
        if self.size() == self.maxSize-1:
            return False
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True

    #Removing elements from the queue
    def dequeue(self):
        if self.size()==0:
            return ("Queue Empty!") 
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

    def peek(self):
        if self.size() == 0:
            return None
        data = self.queue[self.head]
        return data


    #Calculating the size of the queue
    def size(self):
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.maxSize - (self.head-self.tail))


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
    def __init__(self, mean_landings=0.6, mean_take_off=0.4, time_laps=10):
        self.mean_landings = mean_landings
        self.mean_take_off = mean_take_off
        self.time_laps = time_laps 
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

    # Initialiserer kjøringen av algoritmen. Oppretter kø-objekter og starter simuleringen.
    def initialize(self):
        self.in_traffic = CircularQueue()
        self.on_ground = CircularQueue()
        self.time_step() 

    def time_step(self):
        for step in range(self.time_laps):
            separator = "[Tidssteg {}]".format(step)
            print(separator.center(58, '-'))
            self.generate_new_planes(self.in_traffic, self.mean_landings)
            self.generate_new_planes(self.on_ground, self.mean_take_off)
            # Prioriterer flyene i luften slik oppgaven ber om
            if self.in_traffic.peek():
               # self.in_traffic = 
                self.handle_plane(self.in_traffic, 'landing', 'landet')
                self.total_planes_landed += 1
            elif self.on_ground.peek():
               # self.on_ground = 
                self.handle_plane(self.on_ground, 'avgang', 'tok av')
                self.total_planes_take_off += 1
            else:
                print("Ingenting å gjøre".center(58, " "))
            print("\n") 
        self.print_results()


    def print_results(self):
        print("[Resultat]".center(58, "-"))
        self.pretty_print("Simlueringen ferdig etter", "{} tidsenheter".format(self.time_laps))
        self.pretty_print("Totalt antall fly behandlet", self.total_planes_handled)
        self.pretty_print("Antall fly landet", self.total_planes_landed)
        self.pretty_print("Antall fly tatt av", self.total_planes_take_off)
        self.pretty_print("Antall fly avvist", self.total_planes_rejected)
        self.pretty_print("Antall fly klare til landing", self.in_traffic.size())
        self.pretty_print("Antall fly klare til take off", self.on_ground.size())
        print("[Slutt]".center(58, "-"))
        
        
    def pretty_print(self, first, second):
        printer = [str(first).ljust(30, " "), str(second).ljust(3, " ")]
        print(" {} : {}".format(printer[0], printer[1]))


    # queue er køen som blir brukt. Pre er før handling, post er etter.
    # Eks: pre = landing, post = landet
    # Fly 1 klar for _landing_
    # Fly 1 _landet_
    def handle_plane(self, queue, pre, post): 
        if queue.peek():
            plane = queue.peek()
            print("Fly {} klar for {}".format(plane, pre).center(58, " "))
            queue.dequeue()
            print("Fly {} {}".format(plane, post).center(58, " "))

    def generate_new_planes(self, queue, mean):
        amount_of_new_planes = self.get_poisson_random(mean)
        for planes in range(amount_of_new_planes):
            plane = Plane()
            success = queue.enqueue(plane)
            if not success:
                self.total_planes_rejected += 1
                break
            self.total_planes_handled += 1


try:

    time_laps = int(input("[Integer] Hvor mange tidsenheter skal simuleringen gå? : "))
    take_offs_per_time_lap = float(input("[Float < 1.0] Forventet antall ankomster pr. tidsenhet? : "))
    landings_per_time_lap = float(input("[Float < 1.0] Forventet antall avganger pr. tidsenhet? : "))
except: 
    time_laps = 20
    take_offs_per_time_lap = 0.6
    landings_per_time_lap = 0.4
    print("Noe gikk galt med inputs. Bruker defaults")

if take_offs_per_time_lap > 0.9 or landings_per_time_lap > 0.9:
    exit("Forventet antall * pr. tidsenhet kan ikke være høyere enn 0.9")

a = Airport(take_offs_per_time_lap, landings_per_time_lap, time_laps)
a.initialize()


