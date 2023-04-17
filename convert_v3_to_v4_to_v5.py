import pandas as pd
import numpy as np

v4 = pd.read_csv('data/data_v4.csv')
cur_yr_v3 = pd.read_csv('data/data_v3_22_23.csv')

remove = list(set(list(cur_yr_v3.columns)).difference(set(list(v4.columns))))
remove.remove('t1_team')
remove.remove('t2_team')

cur_yr_v4 = cur_yr_v3.drop(columns=remove)
cur_yr_v4['t1_general_traditional_WIN%'] = np.array(cur_yr_v4['t1_general_traditional_WIN%']) * 100
cur_yr_v4['t2_general_traditional_WIN%'] = np.array(cur_yr_v4['t2_general_traditional_WIN%']) * 100

cur_yr_v4.to_csv('data_v5_22_23.csv',index=False)