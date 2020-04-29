import copy
import queue
from collections import defaultdict

""" 
    Alt er i samme fil, da dette er ganske standard i python for mindre prosjekter.
    Høiberg sa det var greit å levere obligen i python, men at klassen måtte oversettes (slik jeg tolket det)
    
    Annen info:
        
        Arrays blir kalt lister i python, og multidimensionale arrays er dictionaries. 
"""

class EnkelGraf:

    def __init__(self, filename):
        self.filename = filename
        self.n = 0
        self.neighbors = defaultdict(int)
        self.data = dict()
        self.preconditions = defaultdict(lambda:0)
        self.no_precondition = dict()

    def get_nodes(self):
        return self.n

    def read(self):
        total_lines = 0
        with open(self.filename) as f:
            total_lines = len(f.readlines())
        self.neighbors = defaultdict(int) 
        # Fyller det andre arrayet (dictionary) med False - tilsvarer linje 57 i java-versjonen
       
        with open(self.filename) as f:
            # Leser første linje og setter den til n
            self.n = int(f.readline())
            for i in range(self.n):
                i = int(i)
                # Setter ALLE nodene til å ha inngrad lik 0. Senere fjerner vi bare de som har fra listen. Litt wonky, men meh
                self.no_precondition[i] = True
                self.neighbors[i] = defaultdict(bool) 
                # Tilsvarer linje 59. Nodene skal være nabo med seg selv.
                self.neighbors[i][i] = True


            self.data = dict()
            # Oppretter to-dimensionalt array. Tilsvarer linje 52-60 i enkelGraf.java
            # Grunnen til at jeg bruker defaultdict og ikke normal dictionary er fordi defaultdict returnerer defaultverdier om du prøver å hente ut en index som ikke er definert (ikke-eksisterende).
            for line in f:
                # Splitter linjen opp i en liste, på mellomrom. Første linje i graf_topsort_2.txt blir da til: [0, MA100, 2, 5, 6]
                lsplit = line.split()
                # Siden vi vet at nodenummeret alltid er det første på linjen, vet vi at den er på index nr 0 når vi splitter linjen
                node_number = int(lsplit[0])
                # Vi vet også at dataen er på index 1
                self.data[node_number] = lsplit[1]
                # Fjerner node_number, data og totalt antall naboer fra listen som holder på linjen
                del lsplit[0:3]
                for neighbor in lsplit:
                    # Fordi python behandler tall i en tekstfil som string, må vi konvertere til int så dict blir [1] og ikke ['1'].
                    neighbor = int(neighbor)
                    # Legger til inngrad til naboen 
                    self.preconditions[neighbor] += 1

                    # Fjerner noden med inngrad > 0 fra listen
                    try:
                        self.no_precondition.pop(neighbor)
                    except KeyError:
                        pass

                    self.neighbors[node_number][neighbor] = True


    def print_output(self):
        for i in range(self.n):
            print(f'{self.data[i]}: ', end='')
            for j, neighbor in enumerate(self.neighbors[i]):
                if self.data[j] and j is not i:
                    print(f'{self.data[j]} ', end='')
            print("")



"""
e = EnkelGraf("graf_topsort_2.txt")
e.read()
e.print_output()
"""

class TopSort(EnkelGraf):

    def __init__(self, filename):
        super().__init__(filename)
        super().read()
        # Fyller arrayet med lengde n med False verdier
        self.visited = [False] * self.n
        self.visited_nodes = list()
        self.order = [None] * self.n
        self.index = self.n - 1
        self.has_edges = [False] * self.n
        self.new_pre = defaultdict()
        self.traversed = defaultdict()
        self.t_queue = queue.LifoQueue()

    def dfs(self, start):
        #self.visited = [False] * self.n
        self.r_dfs(start)

    def r_dfs(self, x):
        self.visited[x] = True
        self.visited_nodes.append(self.data[x])
        #print(self.visited_nodes)
        neighbours = self.neighbors[x]
        if neighbours:
            for neighbour in neighbours:
                if not self.visited[neighbour]:
                    self.r_dfs(neighbour)
        """
        self.visited_nodes.append(self.data[x])
        for y in range(self.n):
            if self.neighbors[x][y] and not self.visited[y]:
                #print(f'{x}, {y} - {self.neighbors[x][y]}')
                self.r_dfs(y)
        return self.data[x]
        """

    
    def r_sort(self):
        node = sorted(self.no_precondition.keys())[-1]
        print(f'Jobber med node {node}: {self.data[node]}')
        node_neighbors = self.neighbors[node]
        for neighbor in node_neighbors:
            preconditions = self.preconditions[neighbor]
            preconditions -= 1
            if preconditions == 0:
                self.no_precondition[neighbor] = True
        self.no_precondition.pop(node)
        self.r_sort()


    def r_sort_old(self, no_p_list):
        
        traversed = dict()
        new_list = dict()
        for node in no_p_list:
            if node not in self.traversed:
                print(f'Jobber med node {node}: {self.data[node]}')
                for node_neighbor in self.neighbors[node]:
                    pre = self.preconditions[node_neighbor]
                    pre -= 1
                    if pre == 0:
                        self.no_precondition[node_neighbor] = True
                        new_list[node_neighbor] = True
        #print(self.no_precondition)
        self.r_sort(new_list)


    def r_sort_stack(self, stack):
        node = stack.pop()
        print(f'Jobber med node {node}: {self.data[node]}')
        node_neighbors = self.neighbors[node]
        for neighbor in node_neighbors:
            if neighbor is not node:
                preconditions = self.preconditions[neighbor]
                preconditions -= 1
                stack.append(neighbor)
                if preconditions == 0:
                    self.no_precondition[neighbor] = True
                self.r_sort_stack(stack)
        if stack:
            self.r_sort_stack(stack)

                

    
    def sort(self):
        stack = list()
        for node in self.no_precondition:
            stack.append(node)

        count = 0

        self.r_sort_stack(stack)
    

    def sort_old(self):
        index = self.n - 1
        order = [None] * self.n
        for at in range(self.n):
            if not self.visited[at]:
                self.dfs(at)
                for node in self.visited_nodes:
                    if node not in order:
                        order[index] = node
                        index -= 1
        print(order)




    
t = TopSort("graf_topsort_2.txt")
t.sort()
#t.sort()
#t.dfs(0)
"""
for i in range(t.get_nodes()):
    t.dfs(i)
print(t.visited)
print(t.order)


"""
