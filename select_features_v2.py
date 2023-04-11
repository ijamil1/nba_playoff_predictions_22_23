import pandas as pd
from sklearn.feature_selection import SelectKBest, mutual_info_classif
import numpy as np
from sklearn.model_selection import train_test_split

k_val = 25
df = pd.read_csv('data/data_v5.csv')
df.drop(columns=['Unnamed: 0.1','Unnamed: 0','Year', 't1_TEAM','t2_TEAM','t1_series_wins','t2_series_wins'],inplace=True)

X = df.drop(columns=['outcome']).to_numpy()
y  = df['outcome'].to_numpy()
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2) #split data into train/test sets 
x_cols = list(df.columns)
x_cols.remove('outcome')

x_train_df = pd.DataFrame(x_train, columns= x_cols)

x_test_df = pd.DataFrame(x_test, columns = x_cols)

y_train_df = pd.DataFrame(y_train,columns=['outcome'])
y_train_df.to_csv('data/y_train_v2.csv')

y_test_df = pd.DataFrame(y_test, columns=['outcome'])
y_test_df.to_csv('data/y_test_v2.csv')

#select k best features by mi score on training data 
k_best = SelectKBest(mutual_info_classif,k=k_val).fit(x_train_df.to_numpy(),y_train_df.to_numpy())
selected_fts = k_best.get_feature_names_out()
fts_list = []
for s in selected_fts:
    fts_list.append(int(s[1:]))

subset_cols = []
for idx in fts_list:
    feature = x_cols[idx]
    if 't1' in feature:
        suffix = feature[feature.find('t1_')+3:]
    else:
        suffix = feature[feature.find('t2_')+3:]
    t1_ft = 't1_'+suffix
    t2_ft = 't2_'+suffix
    if t1_ft not in subset_cols:
        subset_cols.append(t1_ft)
    if t2_ft not in subset_cols:
        subset_cols.append(t2_ft)

subset_xtrain = x_train_df.loc[:,subset_cols]
subset_xtrain.to_csv('data/x_train_v2.csv')

subset_xtest = x_test_df.loc[:,subset_cols]
subset_xtest.to_csv('data/x_test_v2.csv')


