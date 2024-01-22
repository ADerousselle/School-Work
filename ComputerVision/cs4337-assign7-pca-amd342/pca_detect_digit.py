import numpy as np
import cv2
import matplotlib.pyplot as plt


def pca_detect_digit(image, mean_digit, eigenvectors, N):
    """
    Detects the center of a digit in an image using PCA.

    Parameters:
    image (numpy.ndarray): The input image.
    mean_digit (numpy.ndarray): The mean digit image (28x28 array)
    eigenvectors (numpy.ndarray): The eigenvectors of the digit images.
    N (int): The number of eigenvectors to use.

    Returns:
    tuple: The center of the detected digit as a tuple of (row, column) coordinates.
    """
    subwindow_size = 28
    
    # Calculate the mean and standard deviation of the input image
    mean_input_image = np.mean(image)
    std_dev_input_image = np.std(image)
    
    # Normalize the input image using its own mean and standard deviation
    normalized_input_image = (image - mean_input_image) / (std_dev_input_image + 1e-10)

    # Get the dimensions of the input image
    rows, cols = normalized_input_image.shape
    
    #Initialize variables to keep track of the best match
    best_error = float('inf')
    best_center = (0, 0)
    
   # Iterate over subwindows in the input image
    for row in range(rows - subwindow_size + 1):
        for col in range(cols - subwindow_size + 1):
            
            # Extract the subwindow
            subwindow = normalized_input_image[row:row + subwindow_size, col:col + subwindow_size]

            # Convert the subwindow into a 784-dimensional vector
            subwindow_vector = subwindow.reshape(784)
            
            # Normalize the subwindow by subtracting the mean_digit
            normalized_subwindow = subwindow_vector - mean_digit.reshape(784)

            # Project the normalized subwindow onto the top N eigenvectors
            projection = np.dot(normalized_subwindow, eigenvectors[:, :N])

            # Reconstruct the subwindow from the projection
            reconstructed_subwindow = np.dot(projection, eigenvectors[:, :N].T)

            # Calculate the sum of squared differences (SSD) as the reconstruction error
            error = np.sum((subwindow_vector - reconstructed_subwindow) ** 2)

            # If the current SSD is better than the best match, update the best match

            if error < best_error:
                best_error = error
                best_center = (row + subwindow_size // 2, col + subwindow_size // 2)
    
    return best_center
