import sqlite3
import pandas as pd

# establish connection to db
con = sqlite3.connect('pandas-practice/database.db')

# create sql query through connection

df = pd.read_sql_query("SELECT * from purchases", con)
df = df.set_index('index')
print(df)

# saving functions to save to new type of file, can also save new table in database directly using con
# df.to_csv('new_purchases.csv')
# df.to_json('new_purchases.json')
# df.to_sql('new_purchases', con)