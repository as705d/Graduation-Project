import os
import pandas as pd
import numpy as np
import glob
from collections import OrderedDict

#라벨 생성
name = []
y_p = []
#y_pred = np.where(np.array(y_pred) > 0.4, 1, 0)

files = sorted(glob.glob('../datasets/Random_VX/*'))
#count = 0
for file in files:
  #if count < 10000:
    path = os.path.dirname(file)
    base_name = os.path.splitext(os.path.basename(file))[0]
    vir = os.path.splitext(os.path.basename(file))[-1]
    base_name = base_name + vir

    name.append(base_name)
    y_p.append(1)
    #count = count + 1
  #else:
    #break

series = OrderedDict([('hash', name), ('y_pred', y_p)])
result = pd.DataFrame.from_dict(series)
result.to_csv("../labels/Random_Malware10000.csv", index=False)  
print("Label Save")



