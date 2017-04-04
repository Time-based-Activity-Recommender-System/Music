
import numpy as np
import pandas as pd

def main():
    c_cols = ['song_title']
    current_user_data = pd.read_csv('song-titles.txt', sep='\t', names=c_cols) 
    
    d = {'song_id': [0],  'song_title': current_user_data['song_title'][0]}
    df = pd.DataFrame(d)
    df.to_csv('song_titles.txt',sep='\t',index=False, header=False)

    for i in range(1,len(current_user_data)):
        d = {'song_id': [i],  'song_title': current_user_data['song_title'][i]}
        df = pd.DataFrame(d)
        df.to_csv('song_titles.txt',mode='a' ,sep='\t',index=False, header=False)     


if __name__ == "__main__":
    main()