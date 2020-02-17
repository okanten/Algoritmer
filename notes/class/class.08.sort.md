# Sortering

## Insertion sort

Sett på før - Bruker mye tid

Tiden det tar er dataavhengig. Kortere tid om dataen er litt sortert

## Radixsortering

Eksempel på en algoritme som bruker en kø

Krever at du vet ganske mye om dataen. Diskré data. Må også vite spennvidden, antall siffer i tallene

## Hvorfor sortere?

Raskere å søke

## Sorteringsproblemet

Se slide for forelesning (12.02.20)

Sortering er muligens _ikke_ nummer 1 forbruker av prosessortid lenger, etter mediafiler kom på banen. - Motvekt mot det som står på sliden.

## Hvor raskt klarer vi å sortere?

Se slide for forelesning

Umulig å sortere raskere enn O(n log(n))

## Shell sort

Hvilket gap du bruker er det som avgjør hastigheten. Noen gap-størrelser er mer optimale

Shell sort går kjappest om du velger en gap-sekvens på 2.2 - Man vet ikke helt hvorfor

Se slide

O(n * roten av n)


## Optimale

Logaritmiske - rekursivt og "splitt og hersk"

Størrelseorden O(n log(n))

Quicksort er den raskeste algoritmen vi vet om (for generelle data)

Flettesortering er _alltid_ O(n log(n))

### Quicksort

Quicksort bruker lite RAM

Deler arrayet i to, helst på midten. Rekursivt

Bruker første element til å partisjonere delarrayene. 

Partisjoneringsalgoritmen: Se slide

Tre funksjonskall:

findPartition

sorter venstre (rekursiv)

sorter høyre (rekursiv)

### Merge sort / Flettesortering

John von Neumann (1945) - les

Utviklet for å sortere sekvensielle lagringsmedia (f.eks hullkort)

Ikke optimal for arrays - mye swapping og kopiering frem og tilbake

Konge til lenkede lister - minner om gammeldags tape

Garanterer O(n log(n)) effektivitet

Standardimplementasjonen benytter et ekstra array og du må kopiere data frem og tilbake, som gjør den tregere.

 




