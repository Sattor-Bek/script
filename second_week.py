print('Start program...')
import sys
print(sys.version_info)
import numpy as np
import pandas_datareader as pdr

# purchase_1 = pd.Series({'Name': 'Satoru',
#                         'Item': 'Phone',
#                         'Cost': '40,000'})
# purchase_2 = pd.Series({'Name': 'Amelie',
#                         'Item': 'MacBook',
#                         'Cost': '100,000'})
# purchase_3 = pd.Series({'Name': 'Cecile',
#                         'Item': 'PC',
#                         'Cost': '90,000'})
# df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index = ['Shinjuku Yodobashi', 'Mac Store', 'Yamada Denki'])
#
# df = df.set_index([df.index, 'Name'])
# df.index.names = ['Location', 'Name']
# # purchase_4 = pd.Series({'Name':'Taro',
# #                         'Item': 'iPhone',
# #                         'Cost': '50,000',
# #                         'Location': 'Donquijote'})
# # new_df = pd.DataFrame([purchase_4], index=[purchase_4['Location']])
# # new_df = df.append(new_df)
# # print(new_df)
# df = df.append(pd.Series(data = {'Item': 'iPhone', 'Cost': '50,000'}, name =('Donquijote', 'Taro')))
# print(df)
#
# print(df['Cost'].idxmax())
#
#
# print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))
#
#
# # Or alternatively without using a lambda:
# # def totalweight(df, w, q):
# #        return sum(df[w] * df[q])
# #
# # print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))
#
# print(type(df.groupby(level=0)['A','B'])) #<class 'pandas.core.groupby.DataFrameGroupBy'>
# print(type(df.groupby(level=0)['A'])) #<class 'pandas.core.groupby.SeriesGroupBy'>
#
#
# (df.set_index('INDEX').groupby(level=0)['A','B']
#     .agg({'avg': np.average, 'sum': np.sum}))
#
# #
# (df.set_index('INDEX').groupby(level=0)['A','B']
#     .agg({'A': np.average, 'B': np.sum}))
#
# print(Data.pivot_table(index= ['A', 'B'], values=['C','D']))
# print(pd.pivot_table(Data, index=['A','B']))
#
# # TIMESTAMPS
#
# pd.Timestamp('9/1/2016 10:05PM')
# # Timestamp('2016-09-01 22:05:00')
tl = pdr.Series(list('123'), [pdr.Timestamp('2020-01-01'), pdr.Timestamp('2020-01-02'),pdr.Timestamp('2020-01-03')])
print(tl)

dates = pd.date_range('10-01-2016', periods=3, freq='2W-SUN')
# periods = 回数
# freq =頻度

import pandas as pd
import numpy as np

energy = pd.read_csv('energy.csv').set_index('Country').rename(index={"China2": "China", "Australia1": "Australia"})
energy['Energy Supply'] = energy['Energy Supply'] * 1000000

GDP = pd.read_csv('world_bank.csv', skiprows=range(0, 4)).set_index('Country Name').rename(index={"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"})
# print(GDP.head(15))

scimen = pd.read_excel('scimagojr-3.xlsx')
scimen.to_csv("'scimagojr-3.csx", sep=",")
ScimEn = scimen.set_index('Country')

merged = pd.merge(ScimEn, energy, how='outer', left_index=True, right_index=True).sort_values('Rank')
print(merged)
# result = pd.merge(merged, GDP, how='inner', left_index=True, right_index=True)

def answer_one():
    return "ANSWER"
