import cv2
import numpy as np
import matplotlib.pyplot as plt

def remove_holes(my_image):
    """
    Removes holes from a binary image.

    Parameters:
    my_image (numpy.ndarray): A binary image represented as a 2D numpy array.

    Returns:
    numpy.ndarray: The input image with holes removed.
    """

    #Check if the image is all white, if so return the all white image
    if np.all(my_image == 1):
            return my_image
    
    # Create the negation of the input image
    neg_img = np.logical_not(my_image).astype(np.uint8)

    # Find connected components in the negation
    retval, labels = cv2.connectedComponents(neg_img, connectivity=4)

    # Identify the background label (0)
    background_label = labels[0, 0]

    # Find all labels (connected components) other than the background label
    unique_labels = np.unique(labels)
    unique_labels = unique_labels[unique_labels != background_label]

    # Set all pixels in non-background connected components to white
    for label in unique_labels:
        labels[labels == label] = 255

    # Set the result image B by comparing with 255 (white)
    final_img = (labels == 255).astype(np.uint8)

    return final_img





