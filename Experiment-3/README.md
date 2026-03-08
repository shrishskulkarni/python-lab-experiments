## Experiment Title

String manipulation operations in Python

## Aim

To write a Python program to perform various string operations such as case conversion, slicing, splitting, searching, replacing, and indexing using built‑in string methods.

## Algorithm

1. Read an input string `a` from the user.
2. Print the uppercase version of the string using `a.upper()`.
3. Print the lowercase version of the string using `a.lower()`.
4. Print the title‑case version of the string using `a.title()`.
5. Print the swap‑case version of the string using `a.swapcase()`.
6. Print the capitalized version of the string using `a.capitalize()`.
7. Print the first five characters of the string using slicing `a[:5]`.
8. Print the list of words in the string using `a.split()`.
9. Print the index of the first occurrence of the character `'h'` using `a.find('h')`.
10. Print the string after replacing all occurrences of `'a'` with `'b'` using `a.replace('a', 'b')`.
11. Print the length of the string using `len(a)`.
12. Print the index of the substring `"hi"` using `a.index("hi")`.

## Output

Sample run:

```text
enter a string: hi hello
HI HELLO
hi hello
Hi Hello
HI HELLO
Hi hello
hi he
['hi', 'hello']
3
hi hello
8
0
```
