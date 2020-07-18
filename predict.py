from keras.models import load_model
from keras.layers import Conv2D
import keras
import sys
import numpy as np
from PIL import Image

classes = ['monkey','boar','crow']
num_classes = len(classes)
image_size = 50

def buil_model():

    model = load_model('./models/animal_cnn_aug_Mon Jul 13 00:47:39 2020.h')
                   
    return model

def main():
    image = Image.open(sys.argv[1])
    image = image.convert('RGB')
    image = image.resize((image_size,image_size))
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
