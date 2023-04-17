import pandas as pd

d = {'Yr': [], 'hs_wins': [], 'ls_wins': [], 'hs_team': [], 'ls_team':[],'hs_seed': [], 'ls_seed': []}
#hs = higher seed = lower numerical value 
for i in range(10):
    #3 known series each conference + 1 unknown for each conf bc of play in
    d['hs_wins'].append(0)
    d['ls_wins'].append(0)
    d['Yr'].append(2023)

d['hs_seed'].append(2)
d['ls_seed'].append(7)
d['hs_team'].append('Memphis Grizzlies')
d['ls_team'].append('Los Angeles Lakers')
d['hs_seed'].append(2)
d['ls_seed'].append(7)
d['hs_team'].append('Boston Celtics')
d['ls_team'].append('Atlanta Hawks')

d['hs_seed'].append(3)
d['ls_seed'].append(6)
d['hs_team'].append('Sacramento Kings')
d['ls_team'].append('Golden State Warriors')
d['hs_seed'].append(3)
d['ls_seed'].append(6)
d['hs_team'].append('Philadelphia 76ers')
d['ls_team'].append('Brooklyn Nets')


d['hs_seed'].append(4)
d['ls_seed'].append(5)
d['hs_team'].append('Phoenix Suns')
d['ls_team'].append('Los Angeles Clippers')
d['hs_seed'].append(4)
d['ls_seed'].append(5)
d['hs_team'].append('Cleveland Cavaliers')
d['ls_team'].append('New York Knicks')

d['hs_seed'].append(1)
d['ls_seed'].append(8)
d['hs_team'].append('Denver Nuggets')
d['ls_team'].append('Minnesota Timberwolves')
d['hs_seed'].append(1)
d['ls_seed'].append(8)
d['hs_team'].append('Denver Nuggets')
d['ls_team'].append('Oklahoma City Thunder')

d['hs_seed'].append(1)
d['ls_seed'].append(8)
d['hs_team'].append('Milwaukee Bucks')
d['ls_team'].append('Miami Heat')
d['hs_seed'].append(1)
d['ls_seed'].append(8)
d['hs_team'].append('Milwaukee Bucks')
d['ls_team'].append('Chicago Bulls')

pd.DataFrame(d).to_csv('2023_playoffs.csv')