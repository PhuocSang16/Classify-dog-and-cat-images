import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import time
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Đường dẫn tải mô hình
MODEL_PATH = 'Dogs_Cats.keras'

# Tải mô hình
model = load_model(MODEL_PATH)

# Lớp dự đoán
classes = ['Cat', 'Dog']

# Hàm dự đoán ảnh
def predict_image(img_path):
    img = load_img(img_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = img_array.reshape((1, 224, 224, 3))
    img_array = tf.keras.applications.vgg16.preprocess_input(img_array)

    start_time = time.time()
    prediction = model.predict(img_array)[0][0]
    inference_time = time.time() - start_time
    label = "Dog" if prediction > 0.5 else "Cat"
    return label, round(inference_time, 4)
