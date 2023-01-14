import pandas as pd

data = {
    "apples": [4, 2, 6, 5],
    "Oranges": [1, 5, 6, 8]
}

index = ["Aaron", "lee", "steve", "Shaun"]
purchases = pd.DataFrame(data, index=index)

# print(purchases)
# print(type(purchases))

# print(purchases.loc["Aaron"])

dataset = pd.read_csv("dataset.csv")
print(dataset)
