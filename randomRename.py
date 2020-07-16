import os 
import os.path
import glob
import numpy as np
import random

dirs = np.array([])
origin = 'flipedAndNormalDB/'
for file in glob.glob(origin+'*'):
    dirs = np.append(dirs, file)


for i in range(len(dirs)):
    finalRandomName = random.random()
    os.rename(dirs[i],origin+ str(finalRandomName)+'.jpg')



