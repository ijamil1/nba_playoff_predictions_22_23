import pandas as pd

wt_seeds = []
lt_seeds = []
wt_names = []
lt_names = []

def f(ser):
    wt = ser.loc['Winning_Team']
    lt = ser.loc[' Losing_Team']
    wt_seed_str = wt[wt.find('(')+1]
    wt_name = wt[:wt.find('(')-1]
    lt_seed_str = lt[lt.find('(')+1]
    lt_name = lt[:lt.find('(')-1]
    
    wt_names.append(wt_name)
    lt_names.append(lt_name)
    wt_seeds.append(int(wt_seed_str))
    lt_seeds.append(int(lt_seed_str))

df = pd.read_csv('data/playoffs.csv')
df.drop(labels=['Lg','Series','Dates','Filler_1','Filler_2','Favorite','Underdog'],axis=1,inplace=True)
df.apply(f,axis=1)
df.drop(labels=['Winning_Team',' Losing_Team'],axis=1,inplace=True)
df['Winning_Team']=wt_names
df['Losing_Team']=lt_names
df['Winning_Seed']=wt_seeds
df['Losing_Seed']=lt_seeds

df.to_csv('cleaned_playoffs.csv')
