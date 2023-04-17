import pandas as pd
import csv
for st in range(2022, 2023):
    st_str = str(st)
    end = st+1-2000
    if end < 10:
        end_str = '0'+str(end)
    else:
        end_str = str(end)
    datasets = ['general_traditional', 'general_advanced','general_defense','general_opponent','clutch-traditional','clutch-advanced','clutch-opponent']
    df = pd.read_csv('data/'+st_str+'-'+end_str+'_general_traditional'+'.csv')
    try:
        teams = df['TEAM'].tolist() #teams in NBA for st-st+1 season 
    except:
        teams = df['Team'].tolist()
    list_rows = [] #each row is a team
    cols = [] 
    for team in teams: #loop thru each team
        row = []
        for ds in datasets: #for each team, loop thru all available data
            csvf = 'data/'+st_str+'-'+end_str+'_'+ds+'.csv'
            try:
                df = pd.read_csv(csvf)
            except:
                continue
            try:
                team_data = df.loc[df['TEAM']==team] #get data corresponding to team
            except:
                team_data = df.loc[df['Team']==team]
            for idx, value in team_data.items():
                col_name = ds + '_' + idx
                if col_name not in cols:
                    cols.append(col_name)
                row.append(value.iloc[0]) #append data to team specific roww
        list_rows.append(row[:]) #append team specific row to list of rows
    
    #write data to csv file
    with open(st_str+'-'+end_str+'_data.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(cols)
        writer.writerows(list_rows)
