import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Alic", None],
    "Age": [25, 30, None, 25, 22],
    "salary": [50000, 60000, 55000, 50000, None],
}

df = pd.DataFrame(data)

df = df.drop_duplicates()
df = df.dropna()
df.columns = df.columns.str.lower()

print("first rows:\n", df.head())
print("\nInfo:\n")
df.info()
print("\nSummary:\n", df.describe())
