## Experiment Title

Experiment 10

## Aim

To write a program using Pandas to create a DataFrame, clean the data (remove duplicates, remove null values), standardize column names, and display basic DataFrame details.

## Algorithm

1. Import `pandas` as `pd`.
2. Create a dictionary `data` with columns such as `Name`, `Age`, and `salary` including some missing values.
3. Create a DataFrame using `pd.DataFrame(data)`.
4. Remove duplicate rows using `drop_duplicates()`.
5. Remove rows with missing values using `dropna()`.
6. Convert all column names to lowercase using `df.columns.str.lower()`.
7. Display the first few rows using `head()`.
8. Display DataFrame information using `info()`.
9. Display statistical summary using `describe()`.

## Output

Sample output (will vary based on data after cleaning):

```text
first rows:
      name   age   salary
0    Alice  25.0  50000.0
1      Bob  30.0  60000.0
3     Alic  25.0  50000.0

Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   name    3 non-null      object
 1   age     3 non-null      float64
 2   salary  3 non-null      float64
dtypes: float64(2), object(1)
memory usage: ...

Summary:
             age        salary
count   3.000000      3.000000
mean   26.666667  53333.333333
std     2.886751   5773.502692
min    25.000000  50000.000000
25%    25.000000  50000.000000
50%    25.000000  50000.000000
75%    27.500000  55000.000000
max    30.000000  60000.000000
```
