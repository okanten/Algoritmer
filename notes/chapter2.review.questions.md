# Chapter 2: Self Review Questions

## SR 2.1 What is a growth function? What is the purpose of a growth function?

A growth function is the relationship between the problem size and the value we wish to optimize. It represents the _time complexity_ or _space complexity_ of the algorithm.

> A growth function shows time or space utilization relative to the problem size.

### SRA 2.1

> A growth function shows the time or space utilization relative to the problem size. The growth function of an algorithm represents the time complexity of the algorithm.

---

## SR 2.2 What is the asymptotic complexity of an algorithm?

The asymptotic complexity of an algorithm is a way to describe which component/factor that causes the growth in a function. It might be constant (n), logarithmic (log n), exponent(^n) etc.

> A limit on a growth function, defined by the growth function's dominant term; functions similar in asymptotic complexity are grouped into the same general category.

| 		Growth Function 		| 	Order	 	|  Label	|
|-----------------------------------------------|-----------------------|---------------|
|t(n) = 17	         			|O(1)        		| constant	|
|t(n) = 3 log n          			|O(log n) 		| logarithmic	|
|t(n) = 20n - 4          			|O(n)        		| linear	|
|t(n) = 12n log n + 100n 			|O(n log n)  		| n log n	| 
|t(n) = 3n<sup>2</sup> + 5n - 2			|O(n<sup>2</sup>) 	| quadratic	|
|t(n) = 8n<sup>3</sup> + 3n<sup>2</sup> 	|O(n<sup>3</sup>) 	| cubic		|
|t(n) = 2<sup>n</sup> + 18n<sup>2</sup> + 3n 	|O(2<sup>n</sup>) 	| exponential	|

### SRA 2.2 

> Asymptotic complexity gives the changes in the general nature of the function as n or the problem size increases. This characteristic is based on the dominant term of the expression - the term that increases most quickly as n increases.

---

## SR 2.3 How do you define the order of an algorithm? How do you find the order of an algorithm?

You can find the order of an algorithm by removing the constants and everything else but the dominant term from the growth function.

t(n) = 3 log n = O(log n) - 3 is a constant, log n is the dominant term.

t(n) = 2<sup>n</sup> + 18n<sup>2</sup> + 3n = O(2<sup>n</sup>)

> The order of an algorithm is found by eliminating constants and all but the dominant term in the algorithm's growth function

### SRA 2.3

> The order of an algorithm is nothing but the asymptotic complexity of the algorithm. It gives the upper bound to the algorithm's growth function. The order of an algorithm is found by eliminating constants and all but the dominant term in the algorithm's growth function.

---

## SR 2.4 What would be the time complexity of a loop with a logarithmic progression

n + log n

Not sure if we calculate with the constant in a loop (n), but it would be O(1) + O(log n), which can be written as O(log n)

> If the progression of the loop is logarithmic, then its time complexity would be O(log n).

### SRA 2.4

> If the progression of the loop is logarithmic, then its time complexity would be O(log n)

---

## SR 2.5 What would be the time complexity of a loop body that calls a method with a quadratic time complexity?

The time complexity of a loop with a body that calls a method with a quadratic time complexity would be:

O(n) * O(n<sup>2</sup>) = O(n<sup>3</sup>)

### SRA 2.5

> Here the loop structure steps through n items in a linear fashion and the body of the loop is O(n<sup>2</sup>). Therefore, the time complexity of the entire loop is O(n<sup>3</sup>)

---
