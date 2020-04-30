import sys
from collections import defaultdict

""" 
    Alt er i samme fil, da dette er ganske standard i python for mindre prosjekter.
    Høiberg sa det var greit å levere obligen i python, men at klassen måtte oversettes (slik jeg tolket det)
    
    Annen info:
        
        Arrays blir kalt lister i python, og multidimensionale arrays er dictionaries, for matriser bruker man defaultdict. 
        for loops skrives litt annerledes i python,
            for i in range(100) - tilsvarer for (int i = 0; i < 101; i++)
            for name in names - for each - tilsvarer for (String names : numbers) i java
"""

class EnkelGraf:

    def __init__(self, filename):
        self.filename = filename
        self.n = 0
        """
            Her oppretter jeg et to-dimensionalt array for nabo og et dictionary for data. Kunne brukt vanlig liste for data, men foretrekker dict her siden node kan ha navn istedenfor tall
            Grunnen til at jeg bruker defaultdict og ikke normal dictionary er fordi defaultdict returnerer defaultverdier om du prøver å hente ut en index som ikke er definert (ikke-eksisterende).
        """
        self.neighbors = defaultdict(int)
        self.data = dict()

    # Generic getter. Ikke nødvendig, siden man bare kan hente ut n med self.n, men greit likevel.
    def get_nodes(self):
        return self.n

    def read(self):
        # Åpner filen
        with open(self.filename) as f:
            # Leser første linje og setter den til n - første linje er alltid antall noder etter formatet til Høiberg
            self.n = int(f.readline())
            for i in range(self.n):
                i = int(i)
                self.neighbors[i] = defaultdict(bool) 
                # Tilsvarer linje 59. Nodene skal være nabo med seg selv.
                self.neighbors[i][i] = True

            for line in f:
                # Splitter linjen opp i en liste, på mellomrom. Første linje i graf_topsort_2.txt blir da til: [0, MA100, 2, 5, 6]
                lsplit = line.split()
                # Siden vi vet at nodenummeret alltid er det første på linjen, vet vi at den er på index nr 0 når vi splitter linjen
                node_number = int(lsplit[0])
                # Vi vet også at dataen er på index 1
                self.data[node_number] = lsplit[1]
                # Fjerner node_number, data og totalt antall naboer fra listen(arrayet) som holder på linjen
                del lsplit[0:3]
                for neighbor in lsplit:
                    # Fordi python behandler tall i en tekstfil som string, må vi konvertere til int så dict blir [1] og ikke ['1'].
                    neighbor = int(neighbor) 
                    self.neighbors[node_number][neighbor] = True

    # Printer ut grafen. Tilsvarer den i versjonen til høiberg
    def print_output(self):
        for i in range(self.n):
            # , end='' gjør at python ikke skriver ny linje på slutten av utskriften - tilsvarer System.out.print
            print(f'{self.data[i]}: ', end='')
            for j in range(self.n):
                if self.neighbors[i][j] and i is not j:
                    print(f'{self.data[j]} ', end='')
            print("")


class TopSort(EnkelGraf):
  
    def __init__(self, filename):
        super().__init__(filename)
        super().read()
        # Preconditions holder på inngraden til tilsvarende node, altså hvor mange.
        self.preconditions = defaultdict(lambda:0)
        # whichpre holder på hvilke noder som må være "gjort" før tilsvarende node.
        self.whichpre = defaultdict(list)
        self.set_pre_condition()

    def set_pre_condition(self):
        for node_number in range(self.n):
            # Python leser tall fra en fil som str, derfor konverterer vi
            node_number = int(node_number)
            for neighbor in self.neighbors[node_number]:
                neighbor = int(neighbor)
                if node_number is not neighbor:
                    self.preconditions[neighbor] += 1
                    self.whichpre[neighbor].append(node_number)


    # Hold deg fast, er ikke den fineste implementasjonen, men jeg har sitti i mange mange timer så det frister ikke å prøve å gjøre den finere
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
        print("Følgende rekkefølge er lov: ", end='')
        # Skriv ut listen uten [ ] og med pekere istedenfor komma
        print(*stack, sep=' --> ')

# Boilerplate. Sørger for at ikke koden under kjører om man importer filen til en annen.
# Basically: Hvis filen blir kalt på i terminalen, kjør denne koden.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Filnavn: ")
    t = TopSort(filename)
    t.find_and_print()


