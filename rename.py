import os 
import os.path
import glob
import numpy as np

dirs = np.array([])
origin = 'dataset/'
for file in glob.glob(origin+'*'):
    dirs = np.append(dirs, file)

print(dirs)

for i in range(len(dirs)):
    os.rename(dirs[i],origin+ str(i))
