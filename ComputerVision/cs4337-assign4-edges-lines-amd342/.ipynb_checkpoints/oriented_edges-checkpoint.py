import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from gradient_orientations import gradient_orientations

def oriented_edges(image, sigma, threshold, direction, tolerance):
    """
    Detects oriented edges in a grayscale or color image.

    Parameters:
    img (numpy.ndarray): The input image. If the image is in color, it will be converted to grayscale.
    sigma (float): The standard deviation of the Gaussian filter used to blur the image.
    threshold (float): The lower threshold for the Canny edge detector. The upper threshold is twice this value.
    direction (float): The desired direction of the edges, in degrees. The function will detect edges whose direction
        is within `tolerance` degrees from this direction.
    tolerance (float): The tolerance in degrees for the edge direction. The function will detect edges whose direction
        is within this tolerance from the `direction` parameter.

    Returns:
    numpy.ndarray: A binary image where the edge pixels are set to 255 and the non-edge pixels are set to 0.
    """

    #Reduce noise and get an image of just the edges of the original image from Canny.
    img_blur = cv.GaussianBlur(image, (0,0), sigma)
    canny = cv.Canny(img_blur, threshold, 2*threshold)

    #Get orientation(degrees) of each pixel in the original image and normalize it to [0,180) degrees.
    grad_orient_deg = gradient_orientations(image)
    grad_orient_deg = grad_orient_deg % 180

    #Create a blank image the same size and shape as the original to contain our desired edges.
    edge_img = np.zeros_like(image)

    #Iterate through all pixels in the Canny image.
    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            # If the pixel is white, meaning it is part of an edge...
            if canny[i, j] == 255:
                #Calculate the difference between the desired angle of the pixel and the actual angle.
                angle_diff = abs(grad_orient_deg[i, j] - direction)
                
                #If the angle difference is within the allowed distance from the desired angle add the pixel to edg_img.
                if angle_diff <= tolerance:
                    edge_img[i, j] = 255
    return edge_img
