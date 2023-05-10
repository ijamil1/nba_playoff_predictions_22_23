#read in 2023 playoff rd1 matchups; read in season data where each row corresponds to a team, 
# loop thru each playoff matchup, and create data_v1_22_23 csv file where each row corresponds to a playoff
#matchup and contains the regular season data for the teams comprising the matchup  
import pandas as pd
import csv

playoffs = pd.read_csv('data/2023_playoffs_rd2.csv')


list_rows = []
header = []
first=True

yr = 2023
end_yr = yr-2000
if end_yr < 10:
    end_str = '0'+str(end_yr)
else:
    end_str = str(end_yr)
start_yr = yr-1
season_str = str(start_yr)+'-'+end_str
reg_szn = pd.read_csv('data/'+season_str+'_data.csv')
teams = reg_szn.iloc[:,0].tolist()
reg_szn['TEAM']=teams

for idx, pseries in playoffs.iterrows():
    row = []
    row.append(yr)
    if first:
        header.append('Year')
    hst = pseries['hs_team']
    lst = pseries['ls_team']
    if hst < lst:
        t1 = hst
        t2 = lst
        
        
        t1_seed = pseries['hs_seed']
        t2_seed = pseries['ls_seed']
    else:
        t1 = lst
        t2 = hst
       
        
        t1_seed = pseries['ls_seed']
        t2_seed = pseries['hs_seed']

    if t1 == 'Los Angeles Clippers':
            t1_data = reg_szn.loc[reg_szn['TEAM']=='LA Clippers',:]
    else:        
        t1_data = reg_szn.loc[reg_szn['TEAM']==t1,:]
    if t2 == 'Los Angeles Clippers':
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
        
    row.append(t1_seed)
   

    for idx, val in t2_data.items():
        #idx is column name
        if first:
            header.append('t2_'+idx)
        row.append(val.tolist()[0])
    
    if first:
        header.append('t2_seed')
       
    row.append(t2_seed)
   


    first=False

    list_rows.append(row[:])

with open('data_rd2_22_23.csv','w') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(list_rows)