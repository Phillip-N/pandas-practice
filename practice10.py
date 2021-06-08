# Functions
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

# create function
def rating_function(x):
    if x >= 8.0:
        return 'good'
    else:
        return 'bad'

# apply function to a new column
movies_df['rating_category'] = movies_df['rating'].apply(rating_function)
# print(movies_df.head(2))

# can also use lambda to accomplish the same thing
movies_df['rating_category'] = movies_df['rating'].apply(lambda x: 'good' if x>= 8.0 else 'bad')
print(movies_df.head(2))