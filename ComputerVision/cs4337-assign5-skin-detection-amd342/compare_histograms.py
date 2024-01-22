import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from detect_skin import detect_skin
from build_histograms import build_histograms


def compare_histograms():
    """
    Compares two pairs of histograms for skin and non-skin pixels and computes metrics for each pair.
    The histograms are compared on a dataset of images and corresponding ground truth masks.

    Returns:
    metrics (dict): A dictionary containing the following metrics for each pair of histograms:
        - histogram_old_accuracy: The accuracy of the first pair of histograms.
        - histogram_old_TP: The true positives of the first pair of histograms.
        - histogram_old_TN: The true negatives of the first pair of histograms.
        - histogram_old_FP: The false positives of the first pair of histograms.
        - histogram_old_FN: The false negatives of the first pair of histograms.
        - histogram_new_accuracy: The accuracy of the second pair of histograms.
        - histogram_new_TP: The true positives of the second pair of histograms.
        - histogram_new_TN: The true negatives of the second pair of histograms.
        - histogram_new_FP: The false positives of the second pair of histograms.
        - histogram_new_FN: The false negatives of the second pair of histograms.
    """
    
    # Your code here...
    
    
    metrics = {}

    # Uncomment the following lines to assign the metrics to the dictionary once you have computed them
    # metrics["histogram_old_accuracy"] = accuracy1
    # metrics["histogram_old_TP"] = TP1
    # metrics["histogram_old_TN"] = TN1
    # metrics["histogram_old_FP"] = FP1
    # metrics["histogram_old_FN"] = FN1

    # metrics["histogram_new_accuracy"] = accuracy2
    # metrics["histogram_new_TP"] = TP2
    # metrics["histogram_new_TN"] = TN2
    # metrics["histogram_new_FP"] = FP2
    # metrics["histogram_new_FN"] = FN2

    return metrics

def compute_metrics_for_histogram(hist_skin, hist_non_skin):
    all_prob_scores = []
    all_ground_truth = []

    # Initialization
    total_TP, total_TN, total_FP, total_FN = 0, 0, 0, 0

    # Directories
    # Get the absolute path of the script's directory
    current_directory = os.path.abspath(os.path.dirname(__file__))
    base_dir = os.path.join(current_directory, "data", "Face_Dataset")
    image_dirs = [os.path.join("Pratheepan_Dataset", "FacePhoto"), os.path.join("Pratheepan_Dataset", "FamilyPhoto")]
    mask_dirs = [os.path.join("Ground_Truth", "GroundT_FacePhoto"), os.path.join("Ground_Truth", "GroundT_FamilyPhoto")]

    # Iterate over image directories
    for img_dir, mask_dir in zip(image_dirs, mask_dirs):
        image_folder_path = os.path.join(base_dir, img_dir)
        mask_folder_path = os.path.join(base_dir, mask_dir)
        
        for img_name in os.listdir(image_folder_path):
            img_path = os.path.join(image_folder_path, img_name)
            mask_path = os.path.join(mask_folder_path, img_name)

            # Load image
            img_path = os.path.join(image_folder_path, img_name)
            image = cv2.imread(img_path)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Load corresponding ground truth mask (changing extension to .png)
            mask_name = os.path.splitext(img_name)[0] + ".png"
            mask_path = os.path.join(mask_folder_path, mask_name)
            ground_truth = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
            ground_truth = (ground_truth > 0).astype(int) # Binarize the mask

            # Your code here...

    return total_TP, total_TN, total_FP, total_FN

# Call the function and print results
metrics = compare_histograms()
for key, value in metrics.items():
    print("{}: {}".format(key, value))
