import os
import glob
import pandas as pd
import shutil

labels = pd.read_csv('../Challenge_result_label/result.csv')
label = labels.iloc[:,0].tolist()

for name in label:
    
   shutil.copyfile("../Challenge_dataset_2020/Challenge_dataset_2020/" + name, "../Challenge_dataset_2020/copy/" + name)
