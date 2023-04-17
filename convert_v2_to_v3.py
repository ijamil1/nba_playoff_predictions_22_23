#reads in v2 data, renames the opponent points cols that were read in strangely from bs4, and writes to v3
import pandas as pd

renamed_cols = ['t1_general_defense_OPP_PTS_OFF_TOV','t1_general_defense_OPP_PTS_2ND_CHANCE','t1_general_defense_OPP_PTS_FB','t1_general_defense_OPP_PITP','t2_general_defense_OPP_PTS_OFF_TOV','t2_general_defense_OPP_PTS_2ND_CHANCE','t2_general_defense_OPP_PTS_FB','t2_general_defense_OPP_PITP']

df = pd.read_csv('data/data_v2_22_23.csv')
cols = df.columns
idx = 0

for col in cols:
    if 'general_defense_OPP' in col:
        ser = df[col]
        new_name = renamed_cols[idx]
        idx+=1
        df.drop(columns=[col],inplace=True)
        df[new_name]=ser

df.to_csv('data_v3_22_23.csv',index=False)
        