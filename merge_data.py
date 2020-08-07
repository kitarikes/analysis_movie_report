import pandas as pd
import os

datas = os.listdir('data')

print(datas)

df_merged = pd.read_csv(f'data/{datas[0]}')

# print(df_merged)

for i in range(len(datas)):
  if i == 0:
    continue
  data = pd.read_csv(f'data/{datas[i]}')
  df_merged = pd.concat([df_merged, data])

print(df_merged.shape)

df_merged.to_csv('merged_movies.csv', index=False)