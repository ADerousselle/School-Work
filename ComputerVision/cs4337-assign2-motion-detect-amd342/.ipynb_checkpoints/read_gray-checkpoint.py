import cv2
import numpy as np

def read_gray(frame_path):
    """
    Reads an image from the specified file path and converts it to grayscale.

    Args:
        frame_path (str): The file path of the image to be read.

    Returns:
        numpy.ndarray: The grayscale image as a NumPy array.
    """
    frame = cv2.imread(frame_path)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame