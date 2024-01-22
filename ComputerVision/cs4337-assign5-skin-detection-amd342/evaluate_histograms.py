import numpy as np
from detect_skin import detect_skin

def evaluate_histograms(data, skin_hist_rgb, nonskin_hist_rgb, threshold=0.00001):
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
    
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    # Calculate the prior probabilities
    total_pixels = len(data)
    total_skin_pixels = np.sum(skin_hist_rgb)
    total_nonskin_pixels = np.sum(nonskin_hist_rgb)
    
    P_skin = total_skin_pixels / total_pixels
    P_nonskin = total_nonskin_pixels / total_pixels
    
    # Iterate over the dataset
    for pixel in data:
        # Extract B, G, R values and label
        b, g, r, label = pixel
        
        # Calculate the bin indicies for all chanels
        bin_r = int(r * 32 / 256)
        bin_g = int(g * 32 / 256)
        bin_b = int(b * 32 / 256)
    
        # Calculate likelihoods P(RGB | skin) and P(RGB | non-skin) from histograms
        P_RGB_given_skin = skin_hist_rgb[bin_r, bin_g, bin_b]
        P_RGB_given_nonskin = nonskin_hist_rgb[bin_r, bin_g, bin_b]
    
        # Calculate P(skin | RGB) and P(non-skin | RGB) using Bayes' theorem
        P_skin_given_RGB = (P_RGB_given_skin * P_skin) / (P_RGB_given_skin * P_skin + P_RGB_given_nonskin * P_nonskin)
        P_nonskin_given_RGB = 1 - P_skin_given_RGB  # Since P(skin) + P(non-skin) = 1
    

         # Apply the threshold to classify as skin or non-skin
        if P_skin_given_RGB > threshold:
            predicted_label = 1  # Predicted as skin
        else:
            predicted_label = 2  # Predicted as non-skin
        
        # Update metrics based on true and predicted labels
        if label == 1 and predicted_label == 1:
            TP += 1
        elif label == 2 and predicted_label == 2:
            TN += 1
        elif label == 2 and predicted_label == 1:
            FP += 1
        elif label == 1 and predicted_label == 2:
            FN += 1
    
    # Calculate accuracy
    total_samples = len(data)
    ACC = (TP + TN) / total_samples
        
    return ACC, TP, TN, FP, FN
