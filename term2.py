import pandas as pd
import numpy as np

def answer_one():
    return df['A'].idxmax()

def answer_two():
    df['Dif'] = np.abs(df['A'] - df['A.1'])
    return df['Dif'].idxmax()

def answer_three():
    item_to_drop = df.index[(df['A.1'] == 0) | (df['A'] == 0)]
    ans = df.drop(item_to_drop)
    ans['RelativeDif'] = np.abs((ans['A'] - ans['A.1'])/ans['A.2'])
    return ans['RelativeDif'].idxmax()

def answer_four():
    df['Points'] = (df['A.2']*3) + (df['B.2']*2) + (df['C.2']*1)
    return df['Points']


def get_max():
    return df[df['H'] ==50]['H'].value_counts().idxmax()

def answer_six():
     return census_df[census_df['H'] ==50].sort_values(['A', 'B'], ascending = False).groupby('A').apply(lambda d: sum(d.B[:3])).sort_values(ascending = False).index.tolist()

.groupby('A')['B'].apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()
import numpy as np
def abs_get():
    df = census_df[census_df['H'] ==50].set_index('A').loc[:,['B', 'C', 'D', 'E', 'F', 'G']]
    df['DIF'] = np.abs(df.max(axis='columns') - df.min(axis='columns'))
    return df['DIF'].idxmax()


def answer_eight():
    df = census_df[census_df['H'] ==50].loc[((census_df['R'] == 1) | (census_df['R'] == 2)) & (census_df[['A'][:9] =='Washington'])]
    return df


df = pd.DataFrame([{'Name': 'Sattor', 'Product ID': '01', 'Quantity':3},
                   {'Name': 'Amelie', 'Product ID': '02', 'Quantity':2},
                   {'Name': 'Poline', 'Product ID': '03', 'Quantity':10}])
items = pd.DataFrame([{'Product ID': '01', 'Name': 'Cat food', 'Cost':2.50, 'Unit':'USD'},
                      {'Product ID': '01', 'Name': 'Dog food', 'Cost':3.50, 'Unit':'USD'},
                      {'Product ID': '01', 'Name': 'Bird food', 'Cost':0.50, 'Unit':'USD'},])
pd.merge(df, items, how='outer', left_on='Product ID', right_on='Product ID')
print (pd)
