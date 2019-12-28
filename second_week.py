import pandas as pd
purchase_1 = pd.Series({'Name': 'Satoru',
                        'Item': 'Phone',
                        'Cost': '40,000'})
purchase_2 = pd.Series({'Name': 'Amelie',
                        'Item': 'MacBook',
                        'Cost': '100,000'})
purchase_3 = pd.Series({'Name': 'Cecile',
                        'Item': 'PC',
                        'Cost': '90,000'})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index = ['Shinjuku Yodobashi', 'Mac Store', 'Yamada Denki'])

df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
# purchase_4 = pd.Series({'Name':'Taro',
#                         'Item': 'iPhone',
#                         'Cost': '50,000',
#                         'Location': 'Donquijote'})
# new_df = pd.DataFrame([purchase_4], index=[purchase_4['Location']])
# new_df = df.append(new_df)
# print(new_df)
df = df.append(pd.Series(data = {'Item': 'iPhone', 'Cost': '50,000'}, name =('Donquijote', 'Taro')))
print(df)

print(df['Cost'].idxmax())


print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))


# Or alternatively without using a lambda:
# def totalweight(df, w, q):
#        return sum(df[w] * df[q])
#
# print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))

print(type(df.groupby(level=0)['A','B'])) #<class 'pandas.core.groupby.DataFrameGroupBy'>
print(type(df.groupby(level=0)['A'])) #<class 'pandas.core.groupby.SeriesGroupBy'>


(df.set_index('INDEX').groupby(level=0)['A','B']
    .agg({'avg': np.average, 'sum': np.sum}))

#
(df.set_index('INDEX').groupby(level=0)['A','B']
    .agg({'A': np.average, 'B': np.sum}))

print(Data.pivot_table(index= ['A', 'B'], values=['C','D']))
print(pd.pivot_table(Data, index=['A','B']))
