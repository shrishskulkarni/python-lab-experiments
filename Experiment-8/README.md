## Experiment Title

Experiment 8

## Aim

To write a program to demonstrate regular expression operations in Python (`match`, `search`, `findall`, `sub`) and validate a date pattern.

## Algorithm

1. Import the `re` module.
2. Read `doc` input in the format `DD/MM/YY`.
3. Initialize sample strings `passphrase` and `id`, and pattern `brown`.
4. Use `re.match()` to check whether `id` starts with `sk`.
5. Use `re.search()` to check whether `passphrase` contains `brown`.
6. Use `re.findall()` to find all occurrences of `brown` in `passphrase`.
7. Use `re.sub()` to replace `bear` with `cat` in `passphrase`.
8. Extract numbers from `id` using `re.findall("[0-9]+", id)`.
9. Validate `doc` using the regex pattern `\d{2}/\d{2}/\d{2}$` with `re.match()`.
10. Print results for each step.

## Output

Sample run:

```text
DOC (DD/MM/YY): 15/04/26
valid key
passphrase valid case 1
passphrase valid case 2
one brown cat up let brown drop tame
['8408']
valid DOC
```
