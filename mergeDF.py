#https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

import pandas as pd

dummy_data1 = {
        'SSN': [121, 200, 12, 44, 23],
        'Health': ['Disease', 'Drugs', 'Healthy', 'Healthy', 'I'],
        'Name': ['Sam', 'Don', 'Fam', 'Harr', 'Jay']}

df1 = pd.DataFrame(dummy_data1, columns = ['SSN', 'Health', 'Name'])

print(df1)


dummy_data2 = {
        'SSN': [200, 121, 5, 12, 23],
        'User': ['Sman', 'Donny', 'Far', 'jeddi', 'nat'],
        'Location': ['L', 'N', 'P', 'R', 'T']}


df2 = pd.DataFrame(dummy_data2, columns = ['SSN', 'User', 'Location'])

print(df2)

df3 = pd.concat([df1, df2], axis=1)

print(df3)
