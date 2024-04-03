import pandas as pd

# df = pd.Series([100, 200, 300], index=["a", "b", "c"])
# or

print("\nSeries", "-" * 85)
df = pd.Series({"a": 100, "b": 200, "c": 300})
print(df)

print("\n")
print(df["a"])
print("a" in df)

print("\n")
print(df * 2)

print("\nSeries", "-" * 85)
sales = pd.Series([100, 200, 300])
sales.index = ["Jan", "Feb", "Mar"]
print(sales)

print("\nHead", "-" * 85)
print(sales.head(2))

print("\nTail", "-" * 85)
print(sales.tail(2))

print("\nMin", "-" * 85)
print(sales.min())

print("\nMax", "-" * 85)
print(sales.max())

print("\nSum", "-" * 85)
print(sales.sum())

print("\nMean", "-" * 85)
print(sales.mean())

print("\nSpread of the data", "-" * 85)
print(sales.std())

print("\nVar", "-" * 85)
print(sales.var())
