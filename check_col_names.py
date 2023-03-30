import pandas as pd
for st in range(2000, 2022):
    st_str = str(st)
    end = st+1-2000
    if end < 10:
        end_str = '0'+str(end)
    else:
        end_str = str(end)
    datasets = ['general_traditional', 'general_advanced','general_defense','general_opponent','clutch-traditional','clutch-advanced','clutch-opponent','defense-dash-overall','opponent-shots-general','shooting-efficiency']

    for ds in datasets:
        csv = st_str+'-'+end_str+'_'+ds+'.csv'
        try:
            df = pd.read_csv(csv)
            cols = df.columns
            if 'TEAM' not in cols:
                print(st,ds,sep=', ')
        except:
            continue
