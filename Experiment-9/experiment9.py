try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ModuleNotFoundError as e:
    print("Missing required package:", e.name)
    print("Install dependencies and try again:")
    print("  pip install pandas matplotlib")
    raise

# data
SL = [101, 102, 103, 104, 105]
Name = ["Bran", "Jamie", "Baalish", "Jon", "Arya"]

# dataframe
df = pd.DataFrame({
    "SL": SL,
    "Name": Name
})

print(df)

# plotting
plt.figure()
plt.plot(Name, SL)
plt.title("GoT")
plt.xlabel("Name")
plt.ylabel("Greatness")
plt.show()
