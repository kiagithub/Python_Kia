# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:11:37 2016

@author: kia
"""

import pandas as pd
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ml-1m/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('ml-1m/movies.dat', sep='::', header=None, names=mnames)

users[:5]
ratings[:5]
movies[:5]

#merge

data = pd.merge(pd.merge(ratings, users), movies)
data.ix[0]

#pivoting
'''Check this documentation of pandas pivot table function.
There is no parameter named cols. There used to be 'cols' in older version of Pandas.
Now, 'rows' is replaced by 'index' and 'cols' with 'columns'.
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.pivot_table.html
'''

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
mean_ratings[:5]

ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]

active_titles = ratings_by_title.index[ratings_by_title >= 250]
active_titles

mean_ratings = mean_ratings.ix[active_titles]
mean_ratings[:5]

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
top_female_ratings[:10]

#measuring rating disagreement

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
'''
FutureWarning: by argument to sort_index is deprecated, pls use .sort_values(by=...)
'''
sorted_by_diff = mean_ratings.sort_values(by='diff')
sorted_by_diff[:15]

# Reverse order of rows, take first 15 rows
sorted_by_diff[::-1][:15]

# Standard deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()

# Filter down to active_titles
rating_std_by_title = rating_std_by_title.ix[active_titles]

# Order Series by value in descending order
rating_std_by_title.order(ascending=False)[:10]

