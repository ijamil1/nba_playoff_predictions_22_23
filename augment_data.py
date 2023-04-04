import pandas as pd
import numpy as np
def augment(curf,newf):
    curf_1 = 'data/'+curf
    df = pd.read_csv(curf_1)
    cols = df.columns
    rem = []
    for col in cols:
        if 'Unnamed' in col:
            rem.append(col)
    df.drop(columns=rem+['Year','t1_TEAM','t2_TEAM'],inplace=True)

    #goal is to artificially increase the size of the data 
    #method: for each series, add/decrease some epsilon from the data to create x new rows per series where x is
    #equal to the number of total games in the series. of the x new rows, 4 will have outcome associated with whoever won the series
    #and x-4 will have the opposite outcome 
    epsilon_max = 0.5 
    cols = list(df.columns)
    arr_list = []
    for idx, row in df.iterrows(): #loop thru df (outcome still is a col)
        row_arr = row.to_numpy()
        t1_series_wins = int(row['t1_series_wins'])
        t1_new = np.zeros((t1_series_wins,row_arr.shape[0]))
        t2_series_wins = int(row['t2_series_wins'])
        t2_new = np.zeros((t2_series_wins,row_arr.shape[0]))
        for i in range(t1_series_wins): #for each t1 win 
            epsilon = np.random.uniform(-1*epsilon_max,epsilon_max)
            t1_new[i,:] = row_arr + epsilon
            t1_new[i,t1_new.shape[1]-1]=1 #fix outcome variable 
        for i in range(t2_series_wins): #for each t2 win 
            epsilon = np.random.uniform(-1*epsilon_max,epsilon_max)
            t2_new[i,:] = row_arr + epsilon
            t2_new[i,t2_new.shape[1]-1]=0 #fix outcome variable 
        arr_list.append(t1_new)
        arr_list.append(t2_new)
    arr = np.vstack(arr_list)
    new_df = pd.DataFrame(arr,columns=cols)
    new_df.drop(columns=['t1_series_wins','t2_series_wins'],inplace=True)
    newf_1 = 'data/'+newf
    new_df.to_csv(newf_1,index=False)
       


