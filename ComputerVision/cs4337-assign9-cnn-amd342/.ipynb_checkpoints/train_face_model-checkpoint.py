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
    
    # YOUR CODE HERE

    return model, history