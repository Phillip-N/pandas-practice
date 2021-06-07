import pandas as pd

# read movies database
movies_df = pd.read_csv("pandas-practice/IMDB-Movie-Data.csv", index_col='Title')

# print columns by accessing column attribute
print(movies_df.columns)

# rename method can rename columns
movies_df.rename(columns={
    'Runtime (Minutes)': 'Runtime',
    'Revenue (Millions)': 'Revenue_millions'
}, inplace=True)

print(movies_df.columns)

# list comprehension to make all column names lowercase
movies_df.columns = [col.lower() for col in movies_df]
print(movies_df.columns)