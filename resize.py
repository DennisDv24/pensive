import cv2
import numpy as np
import os, os.path
import glob

directory = 'flipedAndNormalDB/'
output_dir = 'resizedDB/'

dirs = np.array([])

for file in glob.glob(directory+'*'):
    dirs = np.append(dirs, file)

for i in range(len(dirs)):
    print(i)
    try:
        img = cv2.imread(dirs[i])
        img_resized = cv2.resize(img, (128,128))
        cv2.imwrite(output_dir+str(i)+'.jpg', img_resized)
    except Exception as e:
        print(str(e))
