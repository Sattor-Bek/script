import pandas as pd
import numpy as np

# def get_max():
#     return df[df['H'] ==50]['H'].value_counts().idxmax()
#
# def answer_six():
#      return census_df[census_df['H'] ==50].sort_values(['A', 'B'], ascending = False).groupby('A').apply(lambda d: sum(d.B[:3])).sort_values(ascending = False).index.tolist()
#
# .groupby('A')['B'].apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()
# import numpy as np
# def abs_get():
#     df = census_df[census_df['H'] ==50].set_index('A').loc[:,['B', 'C', 'D', 'E', 'F', 'G']]
#     df['DIF'] = np.abs(df.max(axis='columns') - df.min(axis='columns'))
#     return df['DIF'].idxmax()
#
#
# def a():
#     df = census_df[census_df['H'] ==50].loc[((census_df['R'] == 1) | (census_df['R'] == 2)) & (census_df[['A'][:9] =='Washington'])]
#     return df


# clients = pd.DataFrame([{'Name': 'Sattor', 'Product ID': '01', 'Quantity':3},
#                    {'Name': 'Amelie', 'Product ID': '02', 'Quantity':2},
#                    {'Name': 'Poline', 'Product ID': '03', 'Quantity':10}])
# items = pd.DataFrame([{'Product ID': '01', 'Name': 'Cat food', 'Cost':2.50, 'Unit':'USD'},
#                       {'Product ID': '02', 'Name': 'Dog food', 'Cost':3.50, 'Unit':'USD'},
#                       {'Product ID': '03', 'Name': 'Bird food', 'Cost':0.50, 'Unit':'USD'},
#                       {'Product ID': '04', 'Name': 'Turtle food', 'Cost':1.00, 'Unit':'USD'}])
# result  = pd.merge(df, items, how='left', left_on='Product ID', right_on='Product ID')
# result['Total'] = result['Cost'] * result['Quantity']
#
# print (result)
