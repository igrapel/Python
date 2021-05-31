import matplotlib.pyplot as plt
import seaborn as sns

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout 
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.metrics import classification_report,confusion_matrix

import tensorflow as tf

import cv2

import numpy as np
import os
import pathlib
import PIL
import PIL.Image

#import tensorflow_datasets as tfds



os.chdir("C:\\Users\\ilang\\OneDrive\\Desktop\\Projects\\Python\\Flags\\data")

# Load the image
#data = plt.imread("Cuba\\Training\\flag(8).png")

#altering image
#data[:, :, 1] = 1
# Display the image
#plt.imshow(data)
#plt.show()

#data_dir = pathlib.Path("C:\\Users\\ilang\\OneDrive\\Desktop\\Projects\\Python\\Flags\\data")
#image_count = list(data_dir.glob('Mexico/*'))
#PIL.Image.open(str(image_count[3]))
#print(len(image_count))

labels = ['Mexico', 'Cuba']
img_size = 224
def get_data(data_dir):
    data = [] 
    for label in labels: 
        path = os.path.join(data_dir, label)
        class_num = labels.index(label)
        print("Image: " + path)
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path, img))[...,::-1] #convert BGR to RGB format
                resized_arr = cv2.resize(img_arr, (img_size, img_size)) # Reshaping images to preferred size
                data.append([resized_arr, class_num])
            except Exception as e:
                print(e)
                
    data = np.array(data, dtype=object)
    print(data[1,0].shape)
    return data

train = get_data('C:\\Users\\ilang\\OneDrive\\Desktop\\Projects\\Python\\Flags\\data\\train')
val = get_data('C:\\Users\\ilang\\OneDrive\\Desktop\\Projects\\Python\\Flags\\data\\test')
print("Loaded Training and Test Set")

print("Graph Inputs")
l = []
for i in train:
    if(i[1] == 0):
        l.append("Mexico")
    else:
        l.append("Cuba")
sns.set_style('darkgrid')
sns.countplot(x=l)
print("Graph Inputs")

plt.figure(figsize = (5,5))
plt.imshow(train[155][0])
plt.title(labels[train[155][1]])


x_train = []
y_train = []
x_val = []
y_val = []

print("Creating x and y values")
for feature, label in train:
  x_train.append(feature)
  y_train.append(label)

for feature, label in val:
  x_val.append(feature)
  y_val.append(label)

print("Normalizing Data")
# Normalize the data
x_train = np.array(x_train) / 255
x_val = np.array(x_val) / 255

x_train.reshape(-1, img_size, img_size, 1)
y_train = np.array(y_train)

x_val.reshape(-1, img_size, img_size, 1)
y_val = np.array(y_val)

print("Training Dimensions: ", np.ndim(x_train))
print("Test Dimensions: ", np.ndim(x_val))

print("Fitting Data")
datagen = ImageDataGenerator(
        featurewise_center=False,  # set input mean to 0 over the dataset
        samplewise_center=False,  # set each sample mean to 0
        featurewise_std_normalization=False,  # divide inputs by std of the dataset
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,  # apply ZCA whitening
        rotation_range = 30,  # randomly rotate images in the range (degrees, 0 to 180)
        zoom_range = 0.2, # Randomly zoom image 
        width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
        horizontal_flip = True,  # randomly flip images
        vertical_flip=False)
  # randomly flip images


datagen.fit(x_train)

print("Modeling")
model = Sequential()
model.add(Conv2D(32,3,padding="same", activation="relu", input_shape=(224,224,3)))
model.add(MaxPool2D())

model.add(Conv2D(32, 3, padding="same", activation="relu"))
model.add(MaxPool2D())

model.add(Conv2D(64, 3, padding="same", activation="relu"))
model.add(MaxPool2D())
model.add(Dropout(0.4))

model.add(Flatten())
model.add(Dense(128,activation="relu"))
model.add(Dense(2, activation="softmax"))

model.summary()

opt = Adam(learning_rate=0.000001)
model.compile(optimizer = opt , loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True) , metrics = ['accuracy'])

history = model.fit(x_train,y_train,epochs = 500 , validation_data = (x_val, y_val))
model.save("C:\\Users\\ilang\\OneDrive\\Desktop\\Projects\\Python\\Flags")


acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(500)

plt.figure(figsize=(15, 15))
plt.subplot(2, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(2, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
