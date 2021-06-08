# plotting
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger

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

# create a scatter plot to show relationship between ratings and revenue
# movies_df.plot(kind='scatter', x='rating', y='revenue_millions', title='Revenue (millions) vs Rating')
# plt.show()

# create simple histogram based on single column
# movies_df['rating'].plot(kind='hist', title='Rating')
# plt.show()

# creating a box plot to view interquartile ranges
# movies_df['rating'].plot(kind='box')
# plt.show()

# can also create box plots that are grouped by categories
movies_df.boxplot(column='revenue_millions', by='rating_category')
plt.show()