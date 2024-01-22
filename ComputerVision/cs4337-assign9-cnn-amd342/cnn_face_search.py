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
    
    # Scale the image
    scaled_image = cv2.resize(image, None, fx=1.0/scale, fy=1.0/scale)
    
    # Get the height and width of the scaled image
    scaled_height, scaled_width = scaled_image.shape
    
    # Initialize an array for the scores
    scores = np.zeros((scaled_height, scaled_width))
    
    # Create a list for storing image windows
    windows = []
    
    # Extract windows of the scaled size and normalize them
    for y in range(0, scaled_height - face_size[0]):
        for x in range(0, scaled_width - face_size[1]):
            window = scaled_image[y:y + face_size[0], x:x + face_size[1]]
            window = window.astype('float32')
            window = cv2.normalize(window, None, 0, 1, cv2.NORM_MINMAX)
            windows.append(window)
    
    # Convert the list of windows to a numpy array
    windows = np.array(windows)
    
    # Reshape windows to match the model's required input shape
    windows = windows.reshape(-1, face_size[0], face_size[1], 1)
    
    # Predict using the model
    scores = model.predict(windows)
    
    # Reshape predictions to match the windows
    scores = scores.reshape((scaled_height - face_size[0], scaled_width - face_size[1]))
    
    results = []
    
    # Find the top N results
    for _ in range(result_number):
        max_val = np.max(scores)
        max_idx = np.unravel_index(scores.argmax(), scores.shape)
        row, col = max_idx
        top, left = row*scale, col*scale
        bottom, right = top + face_size[0]*scale, left + face_size[1]*scale
        top, left, bottom, right = int(top), int(left), int(bottom), int(right)
        center_row, center_col = (top + bottom) / 2, (left + right) / 2
    
        results.append((max_val, center_row, center_col, top, bottom, left, right))
    
        # Apply NMS by setting a region around the detected face to 0.0
        row_min = max(0, row - face_size[0])
        row_max = min(scaled_height, row + face_size[0] + 1)
        col_min = max(0, col - face_size[1])
        col_max = min(scaled_width, col + face_size[1] + 1)
        scores[row_min:row_max, col_min:col_max] = 0.0
    
    results = sorted(results, key=lambda x: x[0], reverse=True)
    
    return results, scores