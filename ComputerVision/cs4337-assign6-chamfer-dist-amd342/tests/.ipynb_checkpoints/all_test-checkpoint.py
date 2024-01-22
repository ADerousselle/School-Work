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

from chamfer_search import chamfer_search
from skin_chamfer_search import skin_chamfer_search

def save_image(image, filename):
    output_folder = os.path.join(parent_directory, 'output')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, image)


def setup_module(module):
    color_image_file = os.path.join(parent_directory, 'data', 'clutter1.bmp')
    edge_image_file = os.path.join(parent_directory, 'data', 'clutter1_edges.bmp')
    template_file = os.path.join(parent_directory, 'data', 'template.bmp')
    
    module.color_image = cv2.imread(color_image_file)
    module.color_image = cv2.cvtColor(module.color_image, cv2.COLOR_BGR2RGB)
    module.edge_image = cv2.imread(edge_image_file, cv2.IMREAD_GRAYSCALE)
    module.template = cv2.imread(template_file, cv2.IMREAD_GRAYSCALE)

def test_chamfer_search_scale_1():   
    # Run for scale 1
    scale = 1
    number_of_results = 5
    scores, result_image = chamfer_search(edge_image, template, scale, number_of_results)

    # Check that the minimum score is in Row: 171, Column: 222 with a tolerance of 5 pixels
    min_score = np.min(scores)
    row, col = np.unravel_index(np.argmin(scores, axis=None), scores.shape)
    assert abs(row - 171) <= 5
    assert abs(col - 222) <= 5

    # Save result_image to output folder
    save_image(result_image, 'chamfer_search_scale_1.png')

def test_chamfer_search_scale_1_5():
    # Resize the image and run for scale 1.5
    edge_image_scaled = cv2.resize(edge_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
    # Convert to binary image
    edge_image_scaled = (edge_image_scaled > 0).astype(np.uint8)*255

    scale = 1.5
    number_of_results = 5
    scores, result_image = chamfer_search(edge_image_scaled, template, scale, number_of_results)

    # Check that the minimum score is in Row: 256, Column: 333 with a tolerance of 5 pixels
    min_score = np.min(scores)
    row, col = np.unravel_index(np.argmin(scores, axis=None), scores.shape)
    assert abs(row - 256) <= 5
    assert abs(col - 333) <= 5

    # Save result_image to output folder
    save_image(result_image, 'chamfer_search_scale_1_5.png')

def test_skin_chamfer_search_scale_1():
    # Run for scale 1
    scale = 1
    number_of_results = 1
    scores, result_image = skin_chamfer_search(color_image, edge_image, template, scale, number_of_results)

    # Check that the minimum score is in Row: 84, Column: 143 with a tolerance of 5 pixels
    min_score = np.min(scores)
    row, col = np.unravel_index(np.argmin(scores, axis=None), scores.shape)
    assert abs(row - 84) <= 5
    assert abs(col - 143) <= 5

    # Save result_image to output folder
    save_image(result_image, 'skin_chamfer_search_scale_1.png')


def test_skin_chamfer_search_scale_1_5():
    # Resize the image and run for scale 1.5
    color_image_scaled = cv2.resize(color_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    edge_image_scaled = cv2.resize(edge_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
    # Convert to binary image
    edge_image_scaled = (edge_image_scaled > 0).astype(np.uint8)*255

    scale = 1.5
    number_of_results = 1
    scores, result_image = skin_chamfer_search(color_image_scaled, edge_image_scaled, template, scale, number_of_results)

    # Check that the minimum score is in Row: 126, Column: 215 with a tolerance of 5 pixels
    min_score = np.min(scores)
    row, col = np.unravel_index(np.argmin(scores, axis=None), scores.shape)
    assert abs(row - 126) <= 5
    assert abs(col - 215) <= 5

    # Save result_image to output folder
    save_image(result_image, 'skin_chamfer_search_scale_1_5.png')