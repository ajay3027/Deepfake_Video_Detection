import numpy as np
import tensorflow as tf
import cv2

def load_model(path="models/demo_model.h5"):
    # lightweight model for demo, replace with your trained model
    try:
        model = tf.keras.models.load_model(path)
    except Exception as e:
        print("Warning: model load failed:", e)
        # create a dummy model for demo
        inp = tf.keras.Input(shape=(128,128,3))
        x = tf.keras.layers.Conv2D(8,3,activation='relu')(inp)
        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        out = tf.keras.layers.Dense(1, activation='sigmoid')(x)
        model = tf.keras.Model(inputs=inp, outputs=out)
    return model

def predict_frame(model, frame_rgb):
    # frame_rgb: numpy array in RGB
    img = cv2.resize(frame_rgb, (128,128))
    img = img.astype('float32')/255.0
    pred = model.predict(np.expand_dims(img,0), verbose=0)[0][0]
    return float(pred)  # probability of 'fake'
