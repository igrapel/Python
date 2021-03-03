
import pandas as pd
import datetime 
import os
print(os.getcwd())

a = datetime.datetime(1978, 5, 20)
b = datetime.datetime(1998, 6, 10)
c = datetime.datetime(1967, 10, 12)
d = datetime.datetime(2000, 2, 8)
x= datetime.datetime(2001, 2, 8)

e = datetime.datetime(1999, 5, 20)
f = datetime.datetime(1998, 6, 10)
g = datetime.datetime(2000, 2, 8)
h = datetime.datetime(1990, 12, 8)

healthApp = {
    'SSN': [909, 231, 450, 101, 394],
    'Health Status': ['Incongestion', 'Skin Problems', 'Sprained Ankle', 'Covid', 'Addict'],
    'Last Name': ['Mathes', 'Chavez', 'Donn', 'Xing', 'Smith'],
    'BirthDay': [a, b, c, d, x]
    }

df1 = pd.DataFrame(healthApp, columns = ['SSN', 'Health Status', \
                                         'Last Name', 'BirthDay'])
print(df1)    

chatApp = {
        'Last Name': ['Smith', 'Chavez', 'Xing', 'Hardy'],
        'BirthDay': [e, f, g, h],
        'Purchase': ['Books', 'Video Game', 'Football', 'Video Game'],
        'Location': ['Miami', 'NYC', 'Houston', 'Charlotte']   
    }
    
df2 = pd.DataFrame(chatApp, columns = ['Last Name', 'BirthDay', \
                                       'Purchase', 'Location'])
    
print(df2)    

combined_df = pd.merge(df1, df2, on=['Last Name', 'BirthDay'], how='inner')
print(combined_df)
