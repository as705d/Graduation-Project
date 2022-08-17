import os
import subprocess
import sys



linecount = 0

PATH_inputFolder = "../datasets/Random_VX"
PATH_outputFolder = "../datasets/Random_VX_unpack"
PATH = './DIE/die_lin64_portable/diec.sh '

subprocess.check_call(PATH + PATH_inputFolder + ' > ' + './DIEtest.txt', shell=True)
DIEtest = open('./DIEtest.txt', 'rt',encoding='mac_roman')
DIEtest_List = DIEtest.read().splitlines()

for line in DIEtest_List:
    indexPacker = line.find('packer')
    indexFile = line.find('.vir')

    if indexFile != -1:
        indexFile = indexFile + 4
        line = line[indexFile-36:indexFile]

    if indexPacker != -1:
        packerInfo = line	
        tmpCount = linecount

        while (DIEtest_List[tmpCount].find('.vir') == -1):
                tmpCount = tmpCount - 1

        indexFile = DIEtest_List[tmpCount].find('.vir')
        indexFile = indexFile + 4
        fileName = DIEtest_List[tmpCount][indexFile-36:indexFile]


        if packerInfo.find('UPX') != -1:
            PATH_outputFile = PATH_outputFolder + '/' + fileName
            PATH_inputFile = PATH_inputFolder + '/' + fileName
            print(PATH_inputFile + " is unpacking...")
            print("")
            print("")
            r = subprocess.run(['./upxtool/upx', '-d', '-o', PATH_outputFile,PATH_inputFile])
            print(PATH_outputFile + " is done.")

    linecount += 1

DIEtest.close()
