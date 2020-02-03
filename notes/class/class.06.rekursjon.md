# Rekursjon

Bunn i rekursjon - slutten

## Eksempler

Sierpinskis trekant - får du ikke laget med en for loop. Må kunne programmere rekursivt

Sierpinskis svamp

Babushka-dukker

## Beskrivelse og definisjoner

* Et objekt er rekursivt hvis det er beskrevet med _mindre_ versjoner av seg selv.

* Må ha et sluttpunkt, en bunn i det hele.

## Rekursiv datastruktur

Binært tre

## Rekursiv algoritme: Mergesort

Algoritmen er O(n log n)

* Splitt og hersk

Se illustrasjon i forelesning pdf

## Klassisk eksempel: Fakultet

Fakultet er rekursivt

En av de funksjonene som vokser fortest

## Bak kulissene

For maskinen er det akkurat som vanlige funksjonskall. Bruker [metode]kallstacken.

## Fibonaccitall

Fibonaccitallene er en sekvens med heltall. Tallet i rekka er summen av de to forrige tallene.

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377

Rekursiv fibonacci behandling er et eksempel på en dårlig algoritme

F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub>

### Rekursive fibonaccitall: Effektivitet

Å beregne fibonaccitall rekursivt er lite effektivt. 

* Gjør svært mange _redundante_ beregninger.

* Beregning av F<sub>6</sub> medfører 5 beregninger av F<sub>2</sub>

* Rekursivt fibonacciberegning er et godt eksempel på en lite effektiv algoritme

* Rekursiv fibonacciberegning har Big O notasjon: O(c<sup>n</sup>)

#### Base case:

F1 = 1 og F2 = 1

#### Rekursiv del:

F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub>, så lenge n > 2

#### Java:

```java
public static long fib(int n) {
    if (n <= 2)
        return 1;
    return fib(n - 1), + fib(n - 2);
}
```


## Mandelbrotmengden

Rekursjonskonsept


