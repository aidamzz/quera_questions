import pandas as pd
df = pd.read_csv('train.csv')
print(len(df['playerId'].unique()))  # ans: 160

print('\n# or\n')

print(len(df.playerId.unique()))  # ans: 160

print('\n\n##############################################################################\n\n')

# 2. کدام بازیکن، بیشترین تعداد گُل را زده است؟
df_new = df[df['outcome'] == 'گُل']
print(df_new['playerId'].value_counts)  # ans: p_18 


print('\n# or\n')


df['outcome'] = df['outcome'].apply(lambda r: 1 if r=="گُل" else 0)
print(df.groupby('playerId')['outcome'].sum().nlargest(1))  # ans: p_18 

print('\n\n##############################################################################\n\n')

# 3. کدا‌م‌ بازیکنان به ترتیب، بیشترین نرخ تبدیل شوت به گُل و کمترین آن را داشتند؟

df_shoot = df['playerId'].value_counts()
df_fre = df_new['playerId'].value_counts()

z = 0
for k, v in df_fre.items():
    y = v / df_shoot[k]
    if y > z:
        z = y     
print(z)  # 0.25396825396825395 >>> it's the value of p_18 >>> p_18


z = 0.25396825396825395
for k, v in df_fre.items():
    y = v / df_shoot[k]
    if y < z:
        z = y       
print(z)  # 0.028985507246376812 >>> it's the value of p_147 >>> p_147

# ans: p_18,p_147


print('\n# or\n')

print(df.groupby('playerId')['outcome'].mean().nlargest(1))  # p_18
print(df.groupby('playerId')['outcome'].mean().nsmallest(1))  # p_147

# ans: p_18,p_147
  
print('\n\n##############################################################################\n\n')

# 4. فاصله اقلیدسی دورترین شوت تا مرکز دروازه چه‌قدر بوده‌ است؟ (فقط قسمت عدد صحیح)

import numpy as np

arr_Pythagoras = df[['x', 'y']].values
    
q = 0
for x,y in arr_Pythagoras:
    f = np.sqrt(x**2 + y**2)
    if f > q:
        q = f

print(int(np.floor(q)))  # ans: 71


print('\n# or\n')

from math import sqrt

df['distance'] = df.apply(lambda r: int(sqrt(r.x**2 + r.y**2)), axis=1)
print(df.sort_values(['distance'], ascending=False)[['playerId', 'distance']])  # ans: 71

print('\n\n# END #')
print('\n# Code by Behrooz Ostadaghaee #')