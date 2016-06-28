# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 22:54:54 2016

@author: kia

chapter 1 of Python for Data Analysis
"""

path = 'usagov_data2012-03-16.txt'

open(path).readline()

#===================

import json
path = 'usagov_data2012-03-16.txt'
records = [json.loads(line) for line in open(path)]

records[0]
records[0]['tz']

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]

#====================
from collections import defaultdict

def get_counts(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts
    
counts = get_counts(time_zones)

counts['America/New_York']

len(time_zones)

#===================
# With Panda

from pandas import  DataFrame, Series
import numpy as np
import pandas as pd

frame = DataFrame(records)

frame['tz'][:10]

tz_counts = frame['tz'].value_counts()
tz_counts[:10]

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz ==''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]

tz_counts[:10].plot(kind='barh', rot=0)

#=====================

results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
operating_system[:5]

by_tz_os = cframe.groupby(['tz', operating_system])

agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:10]

#=================
# Use to sort in ascending order
indexer = agg_counts.sum(1).argsort()
indexer[:10]

count_subset = agg_counts.take(indexer)[-10:]
count_subset

count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)