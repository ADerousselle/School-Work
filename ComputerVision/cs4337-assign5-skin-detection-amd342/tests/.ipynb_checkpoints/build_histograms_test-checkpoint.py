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

# def setup_module(module):
#     # Set up code to be run before running any test functions in this module
#     module.data_path = os.path.join('data', 'UCI_Skin_NonSkin.txt')
#     module.data = np.loadtxt(module.data_path)
#     # module.skin_hist_rgb, module.nonskin_hist_rgb = build_histograms(module.data)

def test_build_histograms():
    data_path = os.path.join('data', 'UCI_Skin_NonSkin.txt')
    data = np.loadtxt(data_path)
    skin_hist_rgb, nonskin_hist_rgb = build_histograms(data)

    # Check that the histograms have the correct shape
    assert skin_hist_rgb.shape == (32, 32, 32)
    assert nonskin_hist_rgb.shape == (32, 32, 32)

    # Check that the sum of values of each histogram is equal to 1 (approximately)
    assert np.sum(skin_hist_rgb) == pytest.approx(1)
    assert np.sum(nonskin_hist_rgb) == pytest.approx(1)

    # Check that the values of the histograms are between 0 and 1
    assert np.all(skin_hist_rgb >= 0) and np.all(skin_hist_rgb <= 1)
    assert np.all(nonskin_hist_rgb >= 0) and np.all(nonskin_hist_rgb <= 1)

def test_detect_skin():
    data_path = os.path.join('data', 'UCI_Skin_NonSkin.txt')
    data = np.loadtxt(data_path)
    skin_hist_rgb, nonskin_hist_rgb = build_histograms(data)
    
    # Run skin detection on an image
    image = cv2.imread(os.path.join("data", "Face_Dataset", "Pratheepan_Dataset", "FacePhoto", "Matthew_narrowweb__300x381,0.jpg"))
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    detection = detect_skin(image_rgb, skin_hist_rgb, nonskin_hist_rgb)
    skin_mask = detection > 0.5

    # Save detected skin mask as a PNG image in the output directory
    output_dir = os.path.join(parent_directory, 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'skin_detection.png')
    cv2.imwrite(output_path, skin_mask.astype(np.uint8) * 255)



# Code to run after all test functions in this module have been run
def teardown_module(module):
    pass