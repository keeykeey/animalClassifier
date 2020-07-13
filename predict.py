from keras.models import Sequential
from keras.layers import Conv2d,MaxPooling2D
from keras.layers import Activation,Dropout,Flatten,Dense
from keras.utils import np_utils
import keras
import numpy as np
from PIL import Image

classes = ['monkey','boar','crow']
num_classes = len(classes)
image_size = 50

def buil_model():
    model = Sequential()
    model.add(Conv2D(32,(3,3),padding = 'same',input_size=(50,50,3)))
    model.add(Activation('relu'))
    model.add(Conv2D(32,(3,3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64,(3,3),padding='same'))
    model.add(Actication('relu'))
    model.add(Conv2D(64,(3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu')
    model.add(Dropout(0.5))
    model.add(Dense(3))
    model.add(Activation('softmax'))

    opt = keras.optimizers.rmsprop(lr=0.001,decay=1e-6)

