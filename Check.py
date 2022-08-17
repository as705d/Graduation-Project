import os
import numpy as np

#데이터셋 체크
train_X = np.load('../Challenge_numpy/train_X_Challenge.npy')
#test_X = np.load('../results/test_X.npy')
train_Y = np.load('../Challenge_numpy/Y_train_Challenge.npy')
#test_Y = np.load('../results/Y_test.npy')


print("TrainSet: ", len(train_X))
#print("TestSet: ", len(test_X))
print("Trainlabels: ", len(train_Y))
#print("Testlabels: ", len(test_Y))
