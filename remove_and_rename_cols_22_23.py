#read in data_v1_22_23 csv and drops some cols and writes v2 of data
import pandas as pd

df = pd.read_csv('data/data_v1_22_23.csv')
t1_cols_remove = 't1_general_traditional_Team,t1_general_advanced_TEAM,t1_general_advanced_GP,t1_general_advanced_W,t1_general_advanced_L,t1_general_advanced_MIN,t1_general_traditional_Min,t1_general_defense_TEAM,t1_general_defense_GP,t1_general_defense_W,t1_general_defense_L,t1_general_defense_MIN,t1_general_defense_DEF RTG,t1_general_defense_DREB,t1_general_defense_STL,t1_general_defense_BLK,t1_general_opponent_TEAM,t1_general_opponent_Games Played,t1_general_opponent_Wins,t1_general_opponent_Losses,t1_general_opponent_Minutes Played,t1_clutch-traditional_TEAM,t1_clutch-advanced_TEAM,t1_clutch-advanced_Games Played,t1_clutch-advanced_Wins,t1_clutch-advanced_Losses,t1_clutch-advanced_Minutes Played,t1_clutch-opponent_TEAM,t1_clutch-opponent_Games Played,t1_clutch-opponent_Wins,t1_clutch-opponent_Losses, t1_clutch-opponent_Minutes Played'
t1_cols_remove = t1_cols_remove.replace(', ',',').split(',')
remove = []

for col in t1_cols_remove:
    col_suffix = col[3:]
    t1_col = 't1_'+col_suffix
    t2_col = 't2_'+col_suffix
    remove.append(t1_col)
    remove.append(t2_col)


df.drop(columns=remove,inplace=True) 

df.to_csv('data_v2_22_23.csv')