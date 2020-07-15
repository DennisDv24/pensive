import cv2
import random 
import glob
import os, os.path
import numpy as np

directory = 'dataset/'
output_dir = 'fliped/'

dirs = np.array([])

for file in glob.glob(directory+'*'):
    dirs = np.append(dirs, file)


print('go')
for i in range(len(dirs)):
    img = cv2.imread(dirs[i])
    img_fliped = cv2.flip(img, 1)
    print(i)
    cv2.imwrite(output_dir+str(i)+'.jpg', img_fliped)



