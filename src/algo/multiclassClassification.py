import tensorflow as tf
from tensorflow.keras import layers
from service.datasetReader import readDataset

(x_train, y_train), (x_test, y_test) = readDataset('iris')

model = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(5, )),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='relu')
])

model.compile