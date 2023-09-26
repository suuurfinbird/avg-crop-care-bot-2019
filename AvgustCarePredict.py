#!/venv/bin python
#-*- coding: UTF-8 -*-

import sys
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import configparser

fileName1 = './photo/' + str(sys.argv[1]) +'.jpg'

config = configparser.RawConfigParser()
config.read("./global_config.conf")

# Список классов
classes = config.get("classes", "classes").split(',')

#Размер изображения
img_width, img_height = 224, 224

#Считываем настройки и параметры нейросети
with open("AvgustCare_cnn.json", "r") as json_file:
    loaded_model_json = json_file.read()

loaded_model = tf.keras.models.model_from_json(loaded_model_json)
loaded_model.load_weights("AvgustCare_cnn.h5")

#Компилируем нейросеть
loaded_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])

#Загружаем картинку
img = image.load_img(fileName1, target_size=(img_width, img_height))

#Декодируем картинку
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = x/255

#Прогноз
prediction = loaded_model.predict(x)
predictionLIST = np.around(prediction[0], decimals=2)
for i in predictionLIST:
    print('%.2f' % i, end=' ')
print()
print(classes)
print('patology is', classes[np.argmax(prediction)])
#print(fileName1)
