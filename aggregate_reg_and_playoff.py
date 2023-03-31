import pandas as pd
import csv

playoffs = pd.read_csv('data/cleaned_playoffs.csv')
groupby_obj = playoffs.groupby(['Yr'])

list_rows = []
header = []
first=True

for yr in range(2001,2023):
    end_yr = yr-2000
    if end_yr < 10:
        end_str = '0'+str(end_yr)
    else:
        end_str = str(end_yr)
    start_yr = yr-1
    season_str = str(start_yr)+'-'+end_str
    cur_playoffs = groupby_obj.get_group(yr)
    reg_szn = pd.read_csv('data/'+season_str+'_data.csv')
    teams = reg_szn.iloc[:,0].tolist()
    reg_szn['TEAM']=teams

    for idx, pseries in cur_playoffs.iterrows():
        row = []
        row.append(yr)
        if first:
            header.append('Year')
        wt = pseries['Winning_Team']
        lt = pseries['Losing_Team']
        if wt < lt:
            t1 = wt
            t2 = lt
            t1_wins = pseries['W wins']
            t2_wins = pseries['L wins']
            t1_seed = pseries['Winning_Seed']
            t2_seed = pseries['Losing_Seed']
            outcome = 1
        else:
            t1 = lt
            t2 = wt
            t1_wins = pseries['L wins']
            t2_wins = pseries['W wins']
            t1_seed = pseries['Losing_Seed']
            t2_seed = pseries['Winning_Seed']
            outcome = 0

        if t1 == 'Los Angeles Clippers' and start_yr in [2015,2016,2018,2019,2020]:
                t1_data = reg_szn.loc[reg_szn['TEAM']=='LA Clippers',:]
        else:        
            t1_data = reg_szn.loc[reg_szn['TEAM']==t1,:]
        if t2 == 'Los Angeles Clippers' and start_yr in [2015,2016,2018,2019,2020]:
                t2_data = reg_szn.loc[reg_szn['TEAM']=='LA Clippers',:]
        else:  
            t2_data = reg_szn.loc[reg_szn['TEAM']==t2,:]
    
        for idx, val in t1_data.items():
            #idx is column name
            if first:
                header.append('t1_'+idx)
            '''if len(val.tolist())==0:
                print(t1_data)'''
            row.append(val.tolist()[0])
        
        if first:
            header.append('t1_seed')
            header.append('t1_series_wins')
        row.append(t1_seed)
        row.append(t1_wins)

        for idx, val in t2_data.items():
            #idx is column name
            if first:
                header.append('t2_'+idx)
            row.append(val.tolist()[0])
        
        if first:
            header.append('t2_seed')
            header.append('t2_series_wins')
            header.append('outcome')
        row.append(t2_seed)
        row.append(t2_wins)
        row.append(outcome)


        first=False

        list_rows.append(row[:])

with open('data_v1.csv','w') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(list_rows)