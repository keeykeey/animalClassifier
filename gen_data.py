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
for index,classLabel in enumerate(classes):
    photos_dir = "./" + classLabel
    files = glob.glob(photos_dir + '/*.jpg')
    for i,file in enumerate(files):
        if i >= 200:break
        image = Image.open(file)
        image = image.convert('RGB')
        image = image.resize((image_size,image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)#0,1,2
        
X = np.array(X)
Y = np.array(Y)

x_train,x_test,y_train,y_test = train_test_split(X,Y)
xy = (x_train,x_test,y_train,y_test)
np.save('./animal.npy',xy)

