from keras.models import load_model
import cv2
import numpy as np

"""
Predictor usando la red entrenada.
- Clasifica BASTANTE bien dentro de una sola clase.

Mejoras:
- Solo clasifica en 1 clase:
    - Puede ser por el entrenamiento de la red o no.
    - Puede ser por el modelo (esperemos que no)
- El formato de clasificacion se puede pasar a nombre de la clase con un diccionario de clases.

"""

# Se carga el modelo resultado del entrenamiento previo.
model = load_model('vgg16_1.h5')

# Se compila con algunas metricas de optimización, etc.
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# Se lee y se adapta la imagen al formato de entrada que necesita el modelo.
img = cv2.imread('images/test/test_2.jpg')
img = cv2.resize(img,(256,256))
img = np.reshape(img,[1,256,256,3])

# Predice en un formato np.ndarray ejemplo:([0.000001 0.0000005 0.99999])
classes = model.predict(img)
print(classes)

# De esta manera las clases se muestran [0 0 1]
print(np.round(classes,2))