import pandas as pd

# read movies database
movies_df = pd.read_csv("pandas-practice/IMDB-Movie-Data.csv", index_col='Title')

# head outputs the first five rows, we can pass an argument to designate amount of rows i.e. head(10) for 10 rows
# .tail() will output the last 5 rows

print(movies_df.head())

# retrieving info for the dataframe
# the info function provides details into number of rows & columns, data type, and missing data

movies_info = movies_df.info()
print(movies_info)

# the shape attribute will output a tuple counting rows & columns

print(movies_df.shape)

# checking for duplicates
# appending movies_df to itself to create 1000 duplicate rows
temp_df = movies_df.append(movies_df)
print(temp_df.shape)

# drop_duplicates() will remove all duplicates from the dataframe by creating a copy, if we want to continue using we must assign it to a variable or...
# use inplace
print(temp_df.drop_duplicates().shape)

temp_df.drop_duplicates(inplace=True)
print(temp_df.shape)

# can also use the keep argument in drop duplicates to first: (default) Drop duplicates except for the first occurrence, last: Drop duplicates except for the last occurrence, False: Drop all duplicates