import os
import subprocess
import sys
import glob

PATH_inputFolder = "../datasets/Random_VX"
PATH_outputFolder = "../datasets/Random_VX_unpack"
count = 0

files = sorted(glob.glob("../datasets/Random_VX/*"))
for file in files:
    path = os.path.dirname(file)
    base_name = os.path.splitext(os.path.basename(file))[0]
    vir = os.path.splitext(os.path.basename(file))[-1]
    base_name = base_name + vir
    PATH_outputFile = PATH_outputFolder + '/' + base_name
    PATH_inputFile = PATH_inputFolder + '/' + base_name
    r = subprocess.run(['./upxtool/upx', '-d', '-o', PATH_outputFile, PATH_inputFile])
    count = count + 1

print("Packing File : ", count)




