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

# we can use describe to help us understand our variables
# returns summary of distribution of continuous variables
print(movies_df.describe())

# can also use on category variable for count, unique, top, freq
print(movies_df['genre'].describe())

#value_counts() tells us frequency of values in column
print(movies_df['genre'].value_counts().head(10))

# analyzing bivariate relationships and correlation
# can be done using corr
print(movies_df.corr())