import pandas as pd
import os

# reading csv files
# designate index col as first column
df = pd.read_csv('pandas-practice/purchases.csv', index_col=0)

print(df)