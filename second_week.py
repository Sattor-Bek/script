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


(df.drop(df['Quantity'] == 0)
    .set_index(['Item'])
    .rename(columns={'Weight': 'Weight(oz)'})
