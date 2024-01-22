import numpy as np
import cv2


def cnn_face_search(image, model, face_size, scale, result_number):
    """
    Searches for faces in an image using a convolutional neural network (CNN) model.

    Args:
        image (numpy.ndarray): The input image as a numpy array.
        model (tensorflow.keras.models.Sequential): The CNN model to use for face detection.
        face_size (tuple): A tuple containing the height and width of the face window to use for detection.
        scale (float): The scaling factor to use for the image. The scale is measured with the respect to 
                       the original image face size. For example, if the original image face size is (31, 25) 
                       and the scale is 2.0, then the scaled image face size will be (62, 50).
        result_number (int): The maximum number of results to return.

    Returns:
        tuple: A tuple containing two elements:
            - A list of tuples, where each tuple contains the confidence score, center row and column coordinates 
              of the detected face, and the top, bottom, left, and right coordinates of the bounding box around the face.
            - A numpy array containing the confidence scores for each pixel in the input image.
    """
    
	# YOUR CODE HERE

    return results, scores
