import pandas as pd

# can create own dataframes as dictionary
data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

# declare dataframe, and add index of customers
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

# print dataframe
print(purchases)

# locate function for indexed items
print(purchases.loc['June'])

