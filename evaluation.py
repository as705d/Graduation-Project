import os
import numpy as np
import pandas as pd
import glob
from sklearn.metrics import confusion_matrix, accuracy_score
#정탐률 
result = pd.read_csv("../results/result_test_2019.csv")
y_pred = result.iloc[:,2].tolist()

label = pd.read_csv("../labels/2019_4.csv")
y = label.iloc[:,1].tolist()

accuracy = accuracy_score(y_pred, y)
print("Accuracy: {:.2f}%".format(accuracy * 100))
