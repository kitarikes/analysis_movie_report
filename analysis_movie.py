# -*- coding: utf-8 -*-
"""analysis_movie

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vig8lNhzV8C_498oAWbW0nA5V75XnVUQ
"""

import pandas as pd
import numpy as np

df = pd.read_csv('/content/merged_movies.csv')
df.head()

df['actors'].isnull().sum()

df = df.dropna(subset = ['actors'])

df.head()

actor_li = []
for actors in df['actors']:
  for actor in str(actors).split(','):
    actor_li.append(actor.strip())

from collections import defaultdict
d = defaultdict(int)

for actor in df['actors']:
  for ref_actor in actor_li:
    if ref_actor in actor:
      d[ref_actor]+=1

actor_data = dict(d)

actor_sorted = sorted(actor_data.items(), key=lambda x:x[1], reverse=True)
actor_sorted

