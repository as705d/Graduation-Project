import os
import pandas as pd

#라벨 중복 제거
def csv_read():
    df = pd.read_csv("../labels/23th.csv")
    df['hash'] = df['hash'].str.lower()
    print(len(df))
    df = df.drop_duplicates(['hash'], keep="last")
    
    df.to_csv("../labels/23th.csv", index = False)

if __name__=="__main__":

    csv_read()
