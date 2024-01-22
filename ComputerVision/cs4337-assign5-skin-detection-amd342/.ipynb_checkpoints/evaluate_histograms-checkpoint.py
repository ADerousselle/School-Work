import numpy as np
from detect_skin import detect_skin

def evaluate_histograms(data, skin_hist_rgb, nonskin_hist_rgb, threshold=0.5):
    """
    Evaluates the accuracy of a skin detection model using histograms.

    Args:
        data (numpy.ndarray): The dataset array with shape (N, 4). Each row represents a pixel, and the 
                            columns represent the B, G, R values and the label (1 for skin, 2 for non-skin).
        skin_hist_rgb (np.ndarray): The skin color histogram in RGB format.
        nonskin_hist_rgb (np.ndarray): The non-skin color histogram in RGB format.
        threshold (float, optional): The threshold value for skin detection. Defaults to 0.5.

    Returns:
        tuple: A tuple containing the accuracy, true positives, true negatives, false positives, and false negatives.
    """
    
    # Your code here...
    
    return ACC, TP, TN, FP, FN
