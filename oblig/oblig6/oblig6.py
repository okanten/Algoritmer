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
        self.whichpre = defaultdict(list)
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
                    if node_number is not neighbor:
                        self.whichpre[neighbor].append(int(node_number))
                    # Fjerner noden med inngrad > 0 fra listen
                    try:
                        self.no_precondition.pop(neighbor)
                    except KeyError:
                        pass

                    self.neighbors[node_number][neighbor] = True


    def print_output(self):
        for i in range(self.n):
            print("")
            print(f'{self.data[i]}: ', end='')
            for j in range(self.n):
                if self.neighbors[i][j] and i is not j:
                    print(f'{self.data[j]} ', end='')
            print("")



#e = EnkelGraf("graf_topsort_2.txt")
#e.read()
#e.print_output()


class Node:

    class Edge:

        def __init__(self, node, parent_node):
            self.node = node
            self.parent_node = parent_node


    def __init__(self, number, data, edge=None, parent=None):
        self.number = number
        self.data = data
        if edge is None:
            edge = list()
        self.edge = edge
        self.parent = parent

    def add_edge(self, node):
        node_data = node.data
        node_number = node.number
        node_parent = self
        edge = Node(node_number, node_data, parent=node_parent)
        #new_edge = Edge(node, self)
        self.edge.append(edge)


node_numbers = []
node_numbers.append(0)
node_numbers.append(1)
data = []
data.append("Hallo")
data.append("Nabo")

test_node = Node(node_numbers[0], data[0])
test_node2 = Node(node_numbers[1], data[1])
test_node.add_edge(test_node2)


class TopSort(EnkelGraf):
  
    def __init__(self, filename):
        super().__init__(filename)
        super().read()
        # Fyller arrayet med lengde n med False verdier
        self.visited = [False] * self.n
        self.visited_nodes = list()
        self.node_list = list()
        self.order = [None] * self.n
        self.index = self.n - 1
        self.has_edges = [False] * self.n
        self.new_pre = defaultdict()
        self.traversed = defaultdict()
        self.t_queue = queue.LifoQueue()

    
    def find_pre(self):
        pass


    def add_node(self, node_number):
        node_number = node_number
        node_data = self.data[node_number]
        new_node = Node(node_number, node_data)
        self.node_list.append(new_node)


    def add_edge(self, node, edge_node):
        node


    def b_dfs(self, start):
        self.visited = [False] * self.n
        self.r_dfs(start)
        print("")

    def r_dfs(self, x):
        print(f'{self.data[x]} ', end='')
        self.visited[x] = True
        #self.visited_nodes.append(self.data[x])
        self.visited_nodes.append(x)
        #print(self.visited_nodes)
        for y in range(self.n):
            if self.neighbors[x][y] and not self.visited[y]:
                print(f' er nabo med {self.data[y]}')
                self.r_dfs(y)
        """
        neighbours = self.neighbors[x]
        if neighbours:
            for neighbour in neighbours:
                if not self.visited[neighbour]:
                    self.r_dfs(neighbour)
        
        self.visited_nodes.append(self.data[x])
        for y in range(self.n):
            if self.neighbors[x][y] and not self.visited[y]:
                #print(f'{x}, {y} - {self.neighbors[x][y]}')
                self.r_dfs(y)
        return self.data[x]
        """ 
    
    def r_sort(self, x, visited, stack):
        visited[x] = True
        if self.data[x] is 'INF110':
            print("MATCH")
        for i in self.data:
            if not visited[i] and i is not x and self.data[i] not in stack:
                if self.preconditions[i] < 1:
                    print(f'Appending {self.data[i]}')
                    stack.append(self.data[i])
                elif self.whichpre[i]:
                    for node in self.whichpre[i]:
                        if node is 0:
                            print("HAllO")
                        if self.data[node] in stack:
                            print(self.whichpre[i])
                            self.preconditions[i] -= 1
                            self.whichpre[i].remove(node)
                            self.r_sort(node, visited, stack)
                            #stack.append(self.data[node])
                        else:
                            stack.append(self.data[node])
                            visited[node] = True
                            self.r_sort(x, visited, stack)
                    if self.whichpre[i]:
                        x = self.whichpre[i][0]
                        self.r_sort(x, visited, stack)

    def sort(self):
        visited = [False] * self.n
        stack = list()

        for i in range(self.n):
            if not visited[i]:
                self.r_sort(i, visited, stack)
        print(*stack, sep=', ')

    def r_sort_stack(self, stack):
        node = stack.pop()
        if node not in self.visited:
            self.visited[node] = True
            self.visited_nodes.append(node)
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


    def dfs(self, x): 
        # REVERSER STACK FORDI JEG ER LEI
        stack = []
        #for i in self.preconditions[at]:
        for node in self.neighbors[x]:
            if node in self.no_precondition:
                stack.append(node)
                

        self.r_sort_stack(stack)


    """
    def sort(self):
        stack = list()
        for node in self.no_precondition:
            stack.append(node)

        count = 0

        self.r_sort_stack(stack)
    """

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

    def check_condition(self, t_list):
        for node in t_list:
            if self.precondition[node]:
                stack_work(node)


    
t = TopSort("graf_topsort_1.txt")
#t.sort_old()
#for i in range(t.n):
#    t.b_dfs(i)
#print(t.whichpre)
#print(t.preconditions[1])
t.sort()
#t.dfs(0)
"""
for i in range(t.get_nodes()):
    t.dfs(i)
print(t.visited)
print(t.order)


"""
