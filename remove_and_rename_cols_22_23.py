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




rename = 't1_general_defense_OPP PTS,t1_general_defense_OPP PTS.1, t1_general_defense_OPP PTS.2, t1_general_defense_OPP PTS.3'
rename_cols = rename.replace(', ',',').split(',')
rename_dict = {}
idx = 0
for col in rename_cols:
    col_suffix = col[3:]
    t1_col = 't1_'+col_suffix
    t2_col = 't2_'+col_suffix
    if idx == 0:
        #pts off turnovers
        rename_dict[t1_col] = 't1_general_defense_opp_pts_off_turnovers'
        rename_dict[t2_col] = 't2_general_defense_opp_pts_off_turnovers'
        
    elif idx == 1:
        #pts off second chances
        rename_dict[t1_col] = 't1_general_defense_opp_points_on_second_chances'
        rename_dict[t2_col] = 't2_general_defense_opp_points_on_second_chances'
    elif idx == 2:
        #pts on fast breaks
        rename_dict[t1_col] = 't1_general_defense_opp_points_on_fast_breaks'
        rename_dict[t2_col] = 't2_general_defense_opp_points_on_fast_breaks'
    else:
        #pts in the paint
        rename_dict[t1_col] = 't1_general_defense_opp_points_in_paint'
        rename_dict[t2_col] = 't2_general_defense_opp_points_in_paint'
    idx+=1

df.rename(columns=rename_dict,inplace=True)
df.to_csv('data_v2_22_23.csv')