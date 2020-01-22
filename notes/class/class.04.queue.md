# Queue

Lineær datastruktur

Nytt element legges alltid sist i køen

FIFO

## Anvendelser

* Kryptering/dekryptering

* Simulering av systemer med kø

* I OS brukes køer for å tildele ressurser til prosesser/brukere. (RAM, CPU, printer osv)

* Algoritmer som krever systematisk behandling (riktig rekkefølge. radix-sortering, bredde-først traversering av trær og grafer)

## Kø implementert med enkel array

### Mulig løsning:

* La fronten av køen alltid ligge på index 0

* Hold rede på lengden av køen med en indeksvariabel _rear_

* Sett inn nye elementer på indeks _rear_ og øk denne med 1 for hver insetting - enqueue blir O(1)

### Problem:

* Tar vi ut et element må hele køen flyttes et hakk fremover i arrayen

* Dequeue blir O(n) for en kø med _n_ elementer

* Vi ønsker en løsning der både enqueue og dequeue er O(1)

## Kø implementert med sirkulær array

* Lagrer elementene i køen i en array

* 
