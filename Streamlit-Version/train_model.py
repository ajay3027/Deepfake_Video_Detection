import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam
import os

# Paths
train_dir = "data/frames_train"
img_size = (128, 128)
batch_size = 16
epochs = 10

# Data generators
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    horizontal_flip=True,
    zoom_range=0.2,
)

train_gen = datagen.flow_from_directory(
    train_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

val_gen = datagen.flow_from_directory(
    train_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)

# Model using EfficientNetB0 backbone
base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=img_size+(3,))
x = GlobalAveragePooling2D()(base_model.output)
x = Dropout(0.3)(x)
out = Dense(1, activation='sigmoid')(x)
model = Model(inputs=base_model.input, outputs=out)

# Freeze some layers for faster training
for layer in base_model.layers[:150]:
    layer.trainable = False

# Compile
model.compile(optimizer=Adam(1e-4), loss='binary_crossentropy', metrics=['accuracy'])

# Train
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=epochs
)

# Save the trained model
os.makedirs("models", exist_ok=True)
model.save("models/deepfake_model.h5")

print("✅ Model trained and saved to models/deepfake_model.h5")
