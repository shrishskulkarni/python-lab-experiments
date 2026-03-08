## Experiment Title

List operations in Python

## Aim

To write a Python program to demonstrate basic list operations such as appending, extending, copying, sorting, inserting, removing elements, clearing a list, and slicing assignment.

## Algorithm

1. Initialize list `a = [1, 2, 3, 4]` and list `b = [5, 6, 7, 8]`.
2. Append the value `5` to list `a` using `a.append(5)` and print `a`.
3. Extend list `a` with list `b` using `a.extend(b)` and print `a`.
4. Copy list `b` into `a` using `a = b.copy()` and print `a`.
5. Sort list `a` in descending order using `a.sort(reverse=True)` and print `a`.
6. Insert the value `4` at index `2` in `a` using `a.insert(2, 4)` and print `a`.
7. Remove the first occurrence of `4` from `a` using `a.remove(4)` and print `a`.
8. Clear all elements from list `b` using `b.clear()` and print `b`.
9. Replace the slice `a[1:2]` with `[6, 7]` and print the final list `a`.

## Output

Sample run:

```text
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 5, 6, 7, 8]
[5, 6, 7, 8]
[8, 7, 6, 5]
[8, 7, 4, 6, 5]
[8, 7, 6, 5]
[]
[8, 6, 7, 5]
```
