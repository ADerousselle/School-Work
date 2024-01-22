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
from compare_histograms import compare_histograms

def test_compare_histograms():
    metrics = compare_histograms()

    # If metrics is empty, the function is not implemented. In that case, pass the test automatically and print a message
    if len(metrics) == 0:
        pytest.skip("The compare_histograms function is not implemented yet.")

    assert metrics["histogram_old_accuracy"] > 0.8
    assert metrics["histogram_new_accuracy"] > 0.85

    # Write the test results to a text file in the output directory
    output_dir = os.path.join(parent_directory, 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'compare_histograms.txt')

    with open(output_path, 'w') as f:
        f.write("Accuracy Old Histogram: {:.2f}%\n".format(metrics["histogram_old_accuracy"] * 100))
        f.write("True Positives: {}\n".format(metrics["histogram_old_TP"]))
        f.write("True Negatives: {}\n".format(metrics["histogram_old_TN"]))
        f.write("False Positives: {}\n".format(metrics["histogram_old_FP"]))
        f.write("False Negatives: {}\n".format(metrics["histogram_old_FN"]))

        f.write("\nAccuracy New Histogram: {:.2f}%\n".format(metrics["histogram_new_accuracy"] * 100))
        f.write("True Positives: {}\n".format(metrics["histogram_new_TP"]))
        f.write("True Negatives: {}\n".format(metrics["histogram_new_TN"]))
        f.write("False Positives: {}\n".format(metrics["histogram_new_FP"]))
        f.write("False Negatives: {}\n".format(metrics["histogram_new_FN"]))