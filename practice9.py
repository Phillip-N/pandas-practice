import pandas as pd

movies_df = pd.read_csv('pandas-practice/IMDB-Movie-Data.csv', index_col='Title')

movies_df.rename(columns={
    'Runtime (Minutes)': 'Runtime',
    'Revenue (Millions)': 'Revenue_millions'
}, inplace=True)
movies_df.columns = [col.lower() for col in movies_df]

revenue = movies_df['revenue_millions']

revenue_mean = revenue.mean()

revenue.fillna(revenue_mean, inplace=True)

# this returns a series
genre_col = movies_df['genre']
# print(type(genre_col))

# this returns a data frame, i.e. passing a list of column names
genre_col = movies_df[['genre']]
# print(type(genre_col))

# add another column
subset = movies_df[['genre', 'rating']]
# print(subset.head())

# to get rows we use the loc attribute
prom = movies_df.loc['Prometheus']
# print(prom)

# to get a row at a specific index we use iloc instead
prom = movies_df.iloc[1]
# print(prom)

# can also slice as we would using python
movie_subset = movies_df['Prometheus': 'Sing']
movie_subset = movies_df[1:4]
# print(movie_subset)

# conditional selections, below method would return a column of bolean values for ALL rows
condition = (movies_df['director'] == 'Ridley Scott')
# print(condition.head())

# to filter out rows that dont match the condition
movies_df[movies_df['director'] == 'Ridley Scott']

# conditional selections can also use numerical values
ratings_filter = movies_df[movies_df['rating'] >= 8.6].head(3)
# print(ratings_filter)

# also can use logical operators
director_filter = movies_df[(movies_df['director'] == 'Christopher Nolan') | (movies_df['director'] == 'Ridley Scott')].head()

# can also use isin() method instead
director_filter = movies_df[movies_df['director'].isin(['Christopher Nolan', 'Ridley Scott'])].head()

# using and operator
print(movies_df[
    ((movies_df['year'] >= 2005) & (movies_df['year'] <= 2010))
    & (movies_df['rating'] > 8.0)
    & (movies_df['revenue_millions'] < movies_df['revenue_millions'].quantile(0.25))
])