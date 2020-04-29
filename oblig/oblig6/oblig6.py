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
        self.total_lines = 0
        self.neighbors = defaultdict(int)
        self.data = dict()

    def get_nodes(self):
        return self.n

    def read(self):
        total_lines = 0
        with open(self.filename) as f:
            total_lines = len(f.readlines())
        self.neighbors = defaultdict(int)
        
        # Fyller det andre arrayet (dictionary) med False - tilsvarer linje 57 i java-versjonen
        for i in range(total_lines):
            self.neighbors[i] = defaultdict(bool) 
            # Tilsvarer linje 59. Nodene skal være nabo med seg selv.
            self.neighbors[i][i] = True

        with open(self.filename) as f:
            # Leser første linje og setter den til n
            self.n = int(f.readline())
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
            print(f'{self.data[i]}: ', end='')
            for j, neighbor in enumerate(self.neighbors[i]):
                if self.data[j] and j is not i:
                    print(f'{self.data[j]} ', end='')
            print("")



e = EnkelGraf("graf_topsort_2.txt")
e.read()
e.print_output()

class TopSort(EnkelGraf):

    
