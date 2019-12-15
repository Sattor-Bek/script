def answer_one():
    return df['A'].idxmax()
answer_one()

import numpy as np
def answer_two():
    df['Dif'] = np.abs(df['A'] - df['A.1'])
    return df['Dif'].idxmax()
answer_two()

def answer_three():
    item_to_drop = df.index[df['A.2'] == 0]
    df.drop(item_to_drop)
    df['RelativeDif'] = (df['A'] - df['A.1'])/df['A.2']
    return df['RelativeDif'].idxmax()
answer_three()

def answer_four():
    df['Points'] = (df['A.2']*3) + (df['B.2']*2) + (df['C.2']*1)
    return df['Points']
answer_four()


def get_max():
    return df[df['A'] ==50]['A'].value_counts().idxmax()
get_max()

def answer_six():
     return census_df[census_df['C'] ==50].sort_values(['A', 'B'], ascending = False).groupby('A').apply(lambda d: sum(d.B[:3])).sort_values(ascending = False).index.tolist()
answer_six()
