import os
import sys

# Get the absolute path of the script's directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Get the parent directory
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to sys.path
sys.path.append(parent_directory)

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytest

from build_histograms import build_histograms
from detect_skin import detect_skin
from evaluate_histograms import evaluate_histograms

def test_evaluate_histograms():
    data_path = os.path.join('data', 'UCI_Skin_NonSkin.txt')
    data = np.loadtxt(data_path)
    skin_hist_rgb, nonskin_hist_rgb = build_histograms(data)

    # Evaluate with newly build histograms
    accuracy, TP, TN, FP, FN = evaluate_histograms(data, skin_hist_rgb, nonskin_hist_rgb, threshold=0.5)
    assert accuracy > 0.95

    # Evaluate with old histograms
    # Read histograms
    negative_histogram = np.load('data/negative_histogram.npy')
    positive_histogram = np.load('data/positive_histogram.npy')
    accuracy_hist, TP, TN, FP, FN = evaluate_histograms(data, positive_histogram, negative_histogram, threshold=0.5)
    assert accuracy_hist > 0.95

    # Write the test results to a text file in the output directory
    output_dir = os.path.join(parent_directory, 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'evaluate_histograms.txt')

    with open(output_path, 'w') as f:
        f.write("Accuracy New Histogram: {:.2f}%\n".format(accuracy * 100))
        f.write("True Positives: {}\n".format(TP))
        f.write("True Negatives: {}\n".format(TN))
        f.write("False Positives: {}\n".format(FP))
        f.write("False Negatives: {}\n".format(FN))

        f.write("\nAccuracy Old Histogram: {:.2f}%\n".format(accuracy_hist * 100))
        f.write("True Positives: {}\n".format(TP))
        f.write("True Negatives: {}\n".format(TN))
        f.write("False Positives: {}\n".format(FP))
        f.write("False Negatives: {}\n".format(FN))
