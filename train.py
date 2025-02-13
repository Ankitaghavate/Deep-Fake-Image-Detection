import tensorflow as tf
from tensorflow.keras import layers, models
from utils.preprocessing import preprocess_image
import numpy as np
import os

# Load dataset (replace with your dataset path)


def load_dataset(data_dir):
    images = []
    labels = []

    for label, category in enumerate(['real', 'fake']):
        category_dir = os.path.join(data_dir, category)
        for image_name in os.listdir(category_dir):
            image_path = os.path.join(category_dir, image_name)
            image = preprocess_image(image_path)
            images.append(image)
            labels.append(label)

    return np.array(images), np.array(labels)

# Build CNN model


def build_model(input_shape=(128, 128, 3)):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

# Train the model


def train():
    data_dir = 'data/sample_images'  # Replace with your dataset path
    images, labels = load_dataset(data_dir)

    model = build_model()
    model.fit(images, labels, epochs=10, batch_size=32, validation_split=0.2)

    # Save the model
    model.save('models/pretrained_model.h5')


if __name__ == '__main__':
    train()
