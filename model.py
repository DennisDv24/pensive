import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import keras 
from keras.preprocessing.image import load_img
test_img = load_img('resizedDB/100.jpg')
test_img_array = keras.preprocessing.image.img_to_array(test_img)
print(test_img_array)
print(test_img_array.shape)

#Do for all images an then normalize from [0,255] range to [0,1] range

