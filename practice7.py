import pandas as pd

movies_df = pd.read_csv('pandas-practice/IMDB-Movie-Data.csv', index_col='Title')

movies_df.rename(columns={
    'Runtime (Minutes)': 'Runtime',
    'Revenue (Millions)': 'Revenue_millions'
}, inplace=True)
movies_df.columns = [col.lower() for col in movies_df]

# fetch null cells
# print(movies_df.isnull())

# count number of null cells
# print(movies_df.isnull().sum())

# removes any rows with at least a single null value
# optional inplace parameter
# movies_df.dropna()

# drops all columns with at least 1 null value
# movies_df.dropna(axis=1)

# extract revenue column
revenue = movies_df['revenue_millions']

# input missing values using mean
revenue_mean = revenue.mean()

# fill in null cells for revenue column
# using inplace also affects the original movies_df
revenue.fillna(revenue_mean, inplace=True)


