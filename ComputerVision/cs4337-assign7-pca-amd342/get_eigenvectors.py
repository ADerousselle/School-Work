import numpy as np
import cv2

def get_eigenvectors(data_file_path, digit):
    """
    Computes the mean vector and eigenvectors of the covariance matrix of a given digit in a dataset.

    Args:
        data_file_path (str): The path to the dataset file.
        digit (int): The digit to extract from the dataset.

    Returns:
        tuple: A tuple containing the mean vector and eigenvectors of the covariance matrix.
    """
    
    # Load the data from the CSV file
    data = np.loadtxt(data_file_path, delimiter=',')
    
    # Extract the labels and image data
    labels = data[:, 0]
    images = data[:, 1:]
    
    # Filter the data to get only the images of the specified digit
    digit_images = images[labels == digit]
    
    # Reshape the 28x28 images to 784-dimensional vectors
    digit_images = digit_images.reshape((digit_images.shape[0], 28 * 28))
    
    # Normalize the images to have zero mean and unit variance
    mean_vector = np.mean(digit_images, axis=0)
    normalized_images = digit_images - mean_vector
    
    # Calculate the standard deviation and add a small epsilon to avoid division by zero
    #std_dev = np.std(normalized_images, axis=0)
    #epsilon = 1e-10  # Small epsilon to prevent division by zero
    #std_dev = np.maximum(std_dev, epsilon)
    
    # Calculate the covariance matrix and perform PCA
    covariance_matrix = np.cov(normalized_images, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
    
    # Sort the eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    return mean_vector, eigenvectors