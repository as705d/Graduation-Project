import os
import glob
import numpy as np
import pandas as pd
import shutil
import random

#데이터셋 다른 폴더로 복사
files = sorted(glob.glob('../datasets/180705_VX_Heaven/*'))
count = 0

Random_file = random.sample(files,10000)

for file in Random_file:
    path = os.path.dirname(file)
    base_name = os.path.splitext(os.path.basename(file))[0]
    vir = os.path.splitext(os.path.basename(file))[-1]
    base_name = base_name + vir

    shutil.copyfile("../datasets/180705_VX_Heaven/" + base_name, "../datasets/Random_VX/" + base_name)
 
    

    



