#데이터 정규화
import os
import glob
import pandas as pd
import numpy as np
from keras.utils import to_categorical
import cv2
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
#대회용 정규화 작업 test데이터셋만 뽑음

def Number():

	imgs = []
	label = []
	sorted_label = []

	#이미지 로드
	#data = sorted(glob.glob('../Challenge_dataset_2020/Challenge_Image_1k/*'), key=str.lower)
	data = sorted(glob.glob('../images/10000_Random_unpack/*'), key=str.lower)
	#data = sorted(glob.glob('../images/2018bonsun2/*'), key=str.lower)
	#data = sorted(glob.glob('../images/2018/*'), key=str.lower)

	#라벨 로드
	#labels_main = pd.read_csv('../labels/label.csv')
	#labels_main = pd.read_csv('../labels/2020.csv')
	#labels_main = pd.read_csv('../labels/04_label.csv')
	#labels_main['hash'] = labels_main['hash'].str.lower()
	#labels = labels_main.iloc[:,1].tolist()	
	#print(labels_main)

	#conversion = {0 : 0, 1 : 1}
	
	#num_labels = []
	#num_labels.append([conversion[item] for item in labels])
	
	#num_labels = np.array(num_labels)
	
	#One-hot encoding
	#label_one = to_categorical(num_labels)
	#label_one = label_one.reshape(-1, 2)
	#label_one.shape
	
	#이미지를 Numpy행렬로 변환
	for i in data:
            print(i)
            img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
            
            if img is not None:
               imgs.append(img)

	train_imgs = np.array(imgs)
	#print(train_imgs)
	train_imgs.shape
	#print(train_imgs.shape)

	#데이터 정규화 0~1
	train_images = train_imgs / np.max(train_imgs)
	
	#트레이닝 셋과 테스트 셋으로 분류
	#X_train, X_test, Y_train, Y_test = train_test_split(train_images, label_one, test_size = 0.1, random_state=33)


	#데이터 차원 설정
	#test_X = X_test.reshape(-1, 16384)
	#train_X = X_train.reshape(-1, 50176)
	test_X = train_images.reshape(-1, 50176)
	
	
	#데이터 저장
	#np.save('../results/train_X.npy', train_X)
	np.save('../Random10000_numpy/10000_Random_unpack.npy', test_X)
	#np.save('../results/Y_train.npy', Y_train)
	#np.save('../results/Y_test.npy', Y_test)


if __name__=="__main__":

	Number()

