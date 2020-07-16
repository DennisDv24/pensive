import glob

directory = input()

i = 0

for file in glob.glob(directory+'*'):
    i+=1
    print(i)
