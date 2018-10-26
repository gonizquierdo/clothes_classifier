from keras.models import load_model
from keras.preprocessing import image
import cv2

model_file_path = 'full_model_20_epochs.h5'
model = load_model(model_file_path)
img_path = 'images/gonizquierdo/914698_260313677504327_1048014989_n.jpg'
img = cv2.imread(img_path,0)
img = cv2.resize(img,(28,28))

x = image.img_to_array(img)
x = x.reshape(1,1,28,28).astype( 'float32' )

features = model.predict(x)
print(features)