## Experiment Title

Phone book implementation using dictionary

## Aim

To write a Python program to implement a simple phone book using a dictionary and provide menu‑driven operations to display entries, names, phone numbers, delete an entry, and exit.

## Algorithm

1. Read `n`, the number of entries to be stored in the phone book.
2. Initialize an empty dictionary `dict = {}` and a counter `i = 0`.
3. Repeat while `i < n`:
   - Read a name `x` from the user.
   - Read a phone number `y` from the user.
   - Add the pair to the dictionary using `dict.update({x: y})`.
   - Increment `i` by 1.
4. Start an infinite loop to perform phone book operations.
5. Display a menu and read the user’s choice `p`:
   - `1. Print book`
   - `2. Print names`
   - `3. Print phone numbers`
   - `4. Delete entry`
   - `5. Exit`
6. If `p == 1`, print all items of the dictionary using `dict.items()`.
7. Else if `p == 2`, print all names using `dict.keys()`.
8. Else if `p == 3`, print all phone numbers using `dict.values()`.
9. Else if `p == 4`:
   - Read a name `d` from the user.
   - Delete the corresponding entry using `del dict[d]`.
10. Else if `p == 5`, exit the program using `exit(1)`.
11. Otherwise, print "invalid input".
12. Repeat the menu until the user chooses to exit.

## Output

Sample run:

```text
enter n:2
enter name:Alice
enter phone number:1111111111
enter name:Bob
enter phone number:2222222222
Phone Book Operations:
1.Print book
2.Print names
3.Print phone numbers
4.Delete entry
5.Exit
1
dict_items([('Alice', '1111111111'), ('Bob', '2222222222')])
Phone Book Operations:
1.Print book
2.Print names
3.Print phone numbers
4.Delete entry
5.Exit
2
dict_keys(['Alice', 'Bob'])
Phone Book Operations:
1.Print book
2.Print names
3.Print phone numbers
4.Delete entry
5.Exit
5
```
