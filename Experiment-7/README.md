## Experiment Title

Experiment 7

## Aim

To write a program to demonstrate objects, classes, inheritance, and polymorphism in Python.

## Algorithm

1. Define a base class `A` with method `one()` and print a value.
2. Demonstrate **single-level inheritance** by creating class `B(A)` with method `two()`, create an object, and call both methods.
3. Demonstrate **multiple inheritance** by creating classes `G` and `C(G, A)` with method `three()`, create an object, and call inherited and own methods.
4. Demonstrate **hybrid inheritance** by creating classes `D(A)` and `E(B, D)` with method `five()`, create an object, and call methods from all related classes.
5. Demonstrate **multi-level inheritance** by creating class `F(A)` with method `six()`, create an object, and call inherited and own methods.
6. Demonstrate **hierarchical inheritance** by creating classes `H(A)` and `I(B)` and calling their methods.
7. Demonstrate **polymorphism (method overriding)** by creating class `J` with method `poly()` and class `K(J)` overriding `poly()`, then call it and print results.

## Output

Sample output (values printed by each method call):

```text
2
3
2
7
10
2
3
1
12
2
34
2
38
2
3
38
one: 18
two: 2
```
