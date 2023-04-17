import pandas as pd

train = pd.read_csv('data/data_v5.csv')
test = pd.read_csv('data/data_v5_22_23.csv')

train_cols = list(train.columns)
test_cols = list(test.columns)

only_train = set(train_cols).difference(set(test_cols))
for col in only_train:
    train_cols.remove(col)


ordered_cols = train_cols

test_new = test[ordered_cols]
test_new.to_csv('data_v5_22_23.csv',index=False)