import pandas as pd

d = {'Yr': [], 'hs_wins': [], 'ls_wins': [], 'hs_team': [], 'ls_team':[],'hs_seed': [], 'ls_seed': []}
#hs = higher seed = lower numerical value 
for i in range(4):
    #2 series in each  conference
    d['hs_wins'].append(0)
    d['ls_wins'].append(0)
    d['Yr'].append(2023)

d['hs_seed'].append(6)
d['ls_seed'].append(7)
d['hs_team'].append('Golden State Warriors')
d['ls_team'].append('Los Angeles Lakers')
d['hs_seed'].append(1)
d['ls_seed'].append(4)
d['hs_team'].append('Denver Nuggets')
d['ls_team'].append('Phoenix Suns')

d['hs_seed'].append(5)
d['ls_seed'].append(8)
d['hs_team'].append('New York Knicks')
d['ls_team'].append('Miami Heat')
d['hs_seed'].append(2)
d['ls_seed'].append(3)
d['ls_team'].append('Philadelphia 76ers')
d['hs_team'].append('Boston Celtics')

pd.DataFrame(d).to_csv('2023_playoffs_rd2.csv')