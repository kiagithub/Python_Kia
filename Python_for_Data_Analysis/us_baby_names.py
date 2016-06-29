# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:02:09 2016

@author: kia
"""
import numpy as np
import pandas as pd

names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])

names1880.groupby('sex').births.sum()

# 2010 is the last available year right now
years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

# Concatenate everything into a single DataFrame
names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
total_births.tail()

total_births.plot(title='Total births by sex and year')

#==============

def add_prop(group):
# Integer division floors
    births = group.births
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)

#Sanity check close to 1
np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

#
def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]
    
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)

pieces = []
for year, group in names.groupby(['year', 'sex']):
    pieces.append(group.sort_values(by='births', ascending=False)[:1000])
    
top1000 = pd.concat(pieces, ignore_index=True)

#Analyzing naming Trend

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)

#arbitrary subset
subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year")

#=Why

table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
table.plot(title='Sum of table1000.prop by year and sex', 
           yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
           
#=====

df = boys[boys.year == 2010]
df    

prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()
prop_cumsum[:10] 

prop_cumsum.searchsorted(0.5)   # top 50%

#in 1900 50% rank is much smaller
df = boys[boys.year == 1900]
in1900 = df.sort_values(by='prop', ascending=False).prop.cumsum()
in1900.searchsorted(0.5) + 1

#=======================

def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().searchsorted(q) + 1
    
diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')

diversity.head()
diversity.tail()

diversity=diversity.astype(float) #python 3 problem, in previous step each output is a list
diversity.plot(title="Number of popular names in top 50%")



    





