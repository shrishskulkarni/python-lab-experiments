## Experiment Title

Menu‑driven calculator using functions

## Aim

To write a Python program using a user‑defined function to compute the sum and product of two numbers, and to provide a menu‑driven interface for repeated calculations.

## Algorithm

1. Define a function `calc(x, y)` that returns both the sum `x + y` and the product `x * y`.
2. Start an infinite loop using `while True`.
3. Display a menu with two choices and read the user’s choice `n`:
   - `1. Calculate`
   - `2. Exit`
4. If `n == 1`:
   - Read two integers `x` and `y` from the user.
   - Call the function `calc(x, y)` and store the returned values back in `x` and `y`.
   - Print the sum and the product.
5. Else if `n == 2`:
   - Exit the program using `exit(1)`.
6. Otherwise:
   - Print "invalid input".
7. Continue the loop until the user chooses to exit.

## Output

Sample run:

```text
enter choice: 
1.Calculate
2.Exit
1
enter x:5
enter y:3
8
15
enter choice: 
1.Calculate
2.Exit
2
```
