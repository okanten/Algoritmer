
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


def get_poisson_random(mean):
   r = random
   L = math.exp(-mean)
   k = 0
   p = 1.0
   while p > L:
       p = p * r.random()
       k = k + 1
   return k - 1


in_traffic = Queue()
on_ground = Queue()

print(q.peek())
q.remove()
print(q.peek())

def main():
   t = input("Hvor mange tidssteg?")
   meanz = float(input("Frekvens?"))
   meanz = get_poisson_random(meanz)
   print(meanz)

main()
