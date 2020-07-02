from PIL import Image
import os,glob
import numpy as np
from sklearn.model_selection import train_test_split

classes = ['monkey','boar','crow']
num_classes = len(classes)
image_size = 50


