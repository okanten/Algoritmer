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

    def get_nodes(self):
        return self.n

    def read(self):
        self.neighbors = defaultdict(int)  
        with open(self.filename) as f:
            # Leser første linje og setter den til n
            self.n = int(f.readline())
            for i in range(self.n):
                i = int(i)
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
                    self.neighbors[node_number][neighbor] = True


    def print_output(self):
        for i in range(self.n):
            print("")
            print(f'{self.data[i]}: ', end='')
            for j in range(self.n):
                if self.neighbors[i][j] and i is not j:
                    print(f'{self.data[j]} ', end='')
            print("")


class TopSort(EnkelGraf):
  
    def __init__(self, filename):
        super().__init__(filename)
        super().read()
        self.preconditions = defaultdict(lambda:0)
        self.whichpre = defaultdict(list)
        self.set_pre_condition()

    def set_pre_condition(self):
        for node_number in range(self.n):
            # Python leser tall fra en fil som str, derfor konverterer vi
            node_number = int(node_number)
            print(self.neighbors[node_number])
            for neighbor in self.neighbors[node_number]:
                neighbor = int(neighbor)
                if node_number is not neighbor:
                    self.preconditions[neighbor] += 1
                    self.whichpre[neighbor].append(node_number)


    # Hold deg fast
    def r_sort(self, x, visited, stack):
        visited[x] = True
        for i in self.data:
            if not visited[i] and i is not x and self.data[i] not in stack:
                if self.preconditions[i] < 1:
                    stack.append(self.data[i])
                elif self.whichpre[i]:
                    for node in self.whichpre[i]:
                        if self.data[node] in stack:
                            self.preconditions[i] -= 1
                            self.whichpre[i].remove(node)
                            self.r_sort(node, visited, stack)
                        else:
                            stack.append(self.data[node])
                            visited[node] = True
                            self.r_sort(x, visited, stack)
                    if self.whichpre[i]:
                        x = self.whichpre[i][0]
                        self.r_sort(x, visited, stack)

    # Vet oppgaven ber om camelCase, men ingen bruker camelCase i python - håper det er greit
    def find_and_print(self):
        visited = [False] * self.n
        stack = list()

        for i in range(self.n):
            if not visited[i]:
                self.r_sort(i, visited, stack)
        print(*stack, sep=', ')
    
t = TopSort("graf_topsort_2.txt")
t.find_and_print()

