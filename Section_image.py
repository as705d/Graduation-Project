import os
import lief
import glob
from math import *
from PIL import Image
import cv2
import time
import numpy as np

def section(filename):
	
	allvalues = []
	sectionvalues = []
	sectionent = []
	binaryvalues = [] 
	x = 0
	binary = open(filename, 'rb').read()

	try:
            lief_binary = lief.PE.parse(list(binary))
            #sizeof_code = lief_binary.optional_header.sizeof_codes

	    #파일의 Section Header를 읽어 들임
            for s in lief_binary.sections:
                    entry_section = s.content
                    sectionvalues = entry_section
                    allvalues += sectionvalues                

	except lief.not_found:
            print(filename + " : packing file")
            #file = open('../images/lief.txt', 'w')
            #file.write(filename)
            
	except (lief.bad_format, lief.bad_file, lief.pe_error, lief.parser_error, RuntimeError) as e: #non-pe file
            print(filename + " : not a valid PE file")
            #file = open('../images/liefs.txt', 'w')
            #file.write(filename)
            
	except lief.read_out_of_bound as e:
            binary = open(filename, 'rb').read()
            data = list(binary)
            size = len(data)
            W = ceil(sqrt(size))
            h = int(W)
            K = W * W
            base_name=os.path.splitext(os.path.basename(filename))[0]

            if size > 50176 and size < K: #파일 데이터 크기가 이미지 한변의 길이의 제곱보다 작을 경우 남은 부분은 0byte로 처리 한다.

                image = Image.new('L',(h,h))
                print(image)
                space = K - size
		
                while x < space: #남은 부분은 전부 0으로 처리 
                        data += [0]
                        x = x + 1			
                image.putdata(data)

                imagename = '../images/2020/'+base_name+'.png'
                image.save(imagename)
                src = cv2.imread(imagename, cv2.IMREAD_GRAYSCALE)
                resize_image = cv2.resize(src, dsize=(224, 224), interpolation = cv2.INTER_AREA)
                cv2.imwrite(imagename, resize_image)	

                return 0

            elif size < 50176 and size < K:

                image = Image.new('L',(h,h))
                print(image)
                resize_image = image.resize((224, 224), Image.ANTIALIAS)
                space = K - size
		
                while x < space: #남은 부분은 전부 0으로 처리 
                        data += [0]
                        x = x + 1			
                resize_image.putdata(data)

                imagename = '../images/2020/'+base_name+'.png'
                resize_image.save(imagename)
                return 0

            elif size >= 50176 and size == K: 
		
                image = Image.new('L',(h,h))
                print(image)
                image.putdata(data)

                imagename = '../images/2020/'+base_name+'.png'
                image.save(imagename)
                src = cv2.imread(imagename, cv2.IMREAD_GRAYSCALE)
                resize_image = cv2.resize(src, dsize=(224, 224), interpolation = cv2.INTER_AREA)
                cv2.imwrite(imagename, resize_image)
                return 0

            elif size <= 50176 and size == K:

                image = Image.new('L',(h,h))
                print(image)
                resize_image = image.resize((224, 224), Image.ANTIALIAS)
                resize_image.putdata(data)

                imagename = '../images/2020/'+base_name+'.png'
                resize_image.save(imagename)

                return 0

	except Exception as e:  # everything else (KeyboardInterrupt, SystemExit, ValueError):
            raise   

	if len(allvalues) != 0: #정해진 섹션 영역이 모두 있을 경우 해당 섹션 영역을 반환
	    return allvalues
	else:
            return binaryvalues      

def text_section_image(data, file):
	
	x = 0
	#print(len(data))
	size = len(data) #데이터 크기
	W = ceil(sqrt(size)) #이미지 한 변의 길이
	h = int(W)
	K = W * W     	

	if(W == 0 or h == 0): #뽑아낸 데이터가 아무것도 없을 때
		print("Unable to create image because there is no data")
		
	if size > 50176 and size < K: #파일 데이터 크기가 이미지 한변의 길이의 제곱보다 작을 경우 남은 부분은 0byte로 처리 한다.

		image = Image.new('L',(h,h))
		print(image)

		space = K - size
		
		while x < space: #남은 부분은 전부 0으로 처리 
			data += [0]
			x = x + 1			
		image.putdata(data)

		imagename = file+".png"
		image.save(imagename)
		src = cv2.imread(imagename, cv2.IMREAD_GRAYSCALE)
		resize_image = cv2.resize(src, dsize=(224, 224), interpolation = cv2.INTER_AREA)
		cv2.imwrite(imagename, resize_image)		

		return 0

	elif size < 50176 and size < K:

		image = Image.new('L',(h,h))
		print(image)
		resize_image = image.resize((224, 224), Image.ANTIALIAS)

		space = K - size
		
		while x < space: #남은 부분은 전부 0으로 처리 
			data += [0]
			x = x + 1			
		resize_image.putdata(data)

		imagename = file+".png"
		resize_image.save(imagename)
		return 0

	elif size >= 50176 and size == K: 
		
		image = Image.new('L',(h,h))
		print(image)
		image.putdata(data)

		imagename = file+".png"
		image.save(imagename)
		src = cv2.imread(imagename, cv2.IMREAD_GRAYSCALE)
		resize_image = cv2.resize(src, dsize=(224, 224), interpolation = cv2.INTER_AREA)
		cv2.imwrite(imagename, resize_image)	

		return 0

	elif size <= 50176 and size == K:

		image = Image.new('L',(h,h))
		print(image)
		resize_image = image.resize((224, 224), Image.ANTIALIAS)
		resize_image.putdata(data)

		imagename = file+".png"
	
		resize_image.save(imagename)
		return 0

if __name__=="__main__":

	files = glob.glob('../datasets/test/*')
	#files = glob.glob('../Desktop/oav/*')
	for file in files:
             with open(file, 'r') as f:
                  print(file)
             file_full_path=file #directory file route name
             path=os.path.dirname(file_full_path) # file route road
             base_name=os.path.splitext(os.path.basename(file_full_path))[0] #file name road

             outputFilename=os.path.join("../images/features",base_name)
             #outputFilename=os.path.join("../Desktop/ova",base_name)
             binaryData=section(file_full_path)
		
             if binaryData == 0:
                print("not pe")
             else:
                text_section_image(binaryData, outputFilename)
