# Chapter 2: Self Review Questions

## SR 2.1 What is a growth function? What is the purpose of a growth function?

A growth function is the relationship between the problem size and the value we wish to optimize. It represents the _time complexity_ or _space complexity_ of the algorithm.

> A growth function shows time or space utilization relative to the problem size.

## SR 2.2 What is the asymptotic complexity of an algorithm?

The asymptotic complexity of an algorithm is a way to describe which component/factor that causes the growth in a function. It might be constant (n), logarithmic (log n), exponent(^n) etc.

> A limit on a growth function, defined by the growth function's dominant term; functions similar in asymptotic complexity are grouped into the same general category.

| 		Growth Function 		| 	Order	 	|  Label	|
|-----------------------------------------------|-----------------------|---------------|
|t(n) = 17	         			|O(1)        		| constant	|
|t(n) = 3 log n          			|O(log n) 		| logarithmic	|
|t(n) = 20n - 4          			|O(n)        		| linear	|
|t(n) = 12n log n + 100n 			|O(n log n)  		| n log n	| 
|t(n) = 3n<sup>2</sup> + 5n - 2			|O(n<sup>2</sup> 	| quadratic	|
|t(n) = 8n<sup>3</sup> + 3n<sup>2</sup> 	|O(n<sup>3</sup> 	| cubic		|
|t(n) = 2<sup>n</sup> + 18n<sup>2</sup> + 3n 	|O(2<sup>n</sup> 	| exponential	|

---

## SR 2.3 How do you define the order of an algorithm? How do you find the order of an algorithm?


