from PIL import Image
import os,glob
import numpy as np
from sklearn.model_selection import train_test_split

classes = ['monkey','boar','crow']
num_classes = len(classes)
image_size = 50

#load the data

X = []
Y = []
for index,class in enumerate(classes):
    photos_dir = "./" + class
    files = glob.glob(photos_dir + '/*.jpg')
    for i,file in enumerate(files):
        if i >= 200:break
        image = Image.open(file)
        image = Image.convert('RGB')
        image = Image.resize(image_size)
        data = np.asarray(image)
        X.append(data)
        X=np.array(X)
        Y = np.array(Y)        
        Y.append(index)#0,1,2
        

X = np.array(X)
Y = np.array(y)


