import numpy as np
from sklearn.utils import shuffle
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

def train_face_model(faces, nonfaces):
    """
    Trains a convolutional neural network (CNN) model to classify images as faces or non-faces.

    Args:
    - faces: A numpy array of shape (n_faces, height, width) containing grayscale images of faces.
    - nonfaces: A numpy array of shape (n_nonfaces, height, width) containing grayscale images of non-faces.

    Returns:
    - model: A trained Keras CNN model.
    - history: A Keras history object containing information about the training process.
    """

    # Define a simple CNN model
    model = keras.Sequential([
        layers.Input(shape=(faces.shape[1], faces.shape[2], 1)),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Normalize pixel values to the range [0, 1]
    faces = faces.astype('float32') / 255
    nonfaces = nonfaces.astype('float32') / 255

    # Create labels for the datasets (1 = faces, 0 = non-faces)
    face_labels = np.ones(faces.shape[0])
    nonface_labels = np.zeros(nonfaces.shape[0])

    # Combine the datasets and labels
    X_train = np.concatenate((faces, nonfaces), axis=0)
    y_train = np.concatenate((face_labels, nonface_labels))

    # Shuffle the data
    X_train, y_train = shuffle(X_train, y_train, random_state=42)

    # Reshape data for input to the model
    X_train = X_train.reshape(X_train.shape[0], faces.shape[1], faces.shape[2], 1)

    # Train the model
    history = model.fit(X_train, y_train, epochs=20, batch_size=64)

    return model, history