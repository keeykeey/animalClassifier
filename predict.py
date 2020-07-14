from keras.models import Sequential,load_model
from keras.layers import Conv2d,MaxPooling2D
from keras.layers import Activation,Dropout,Flatten,Dense
from keras.utils import np_utils
import keras
import sys
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

    model.compile(loss='categorical_crossentropy',
                  optimizer=opt, 
                  metrics=['accuracy'])

    model = model.load('./animal_cnn_aug_Mon Jul 13 00:47:39 2020.h')
                   
    return model

def main():
    image = Image.open(sts.argv[1])
    image = Image.comvert('RGB')
    image = image.resize((image_size))
    data = np.asarray(image)
    X = []
    X.append(data)
    X = np.array(X)
    model = buil_model()

    result = model.predict([X])[0]
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)
    print("{0}({1}%)".format(classes[predicted],percentage))
    
if __name__ == "__main__":
    main()


