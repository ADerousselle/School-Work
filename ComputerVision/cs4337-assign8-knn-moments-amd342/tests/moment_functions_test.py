import os
import sys

# Get the absolute path of the script's directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Get the parent directory
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to sys.path
sys.path.append(parent_directory)

import numpy as np
import pytest

from raw_moment import raw_moment
from central_moment import central_moment
from normalized_moment import normalized_moment
from hu_moment import hu_moment

###################################################################################################

@pytest.mark.parametrize("image,i,j,expected", [
    # Test cases
    (np.array([[1]]), 0, 0, 1),  # Single pixel image
    (np.array([[1, 2], [3, 4]]), 0, 0, 10),  # Sum of all pixels
    (np.array([[1, 2], [3, 4]]), 1, 0, 7),  # Weighted sum considering x powers
    (np.array([[1, 2], [3, 4]]), 0, 1, 6),  # Weighted sum considering y powers
    (np.array([[1, 2], [3, 4]]), 1, 1, 4),  # Weighted sum considering both x and y powers
    (np.array([[1, 1], [1, 1]]), 0, 2, 2),  # All ones 2x2 image with y^2 weighting
    (np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 2, 0, 15),  # All ones 3x3 image with x^2 weighting
])
def test_raw_moment(image, i, j, expected):
    result = raw_moment(image, i, j)
    assert np.isclose(result, expected, atol=1e-6), f"Expected {expected}, but got {result}"


###################################################################################################

@pytest.mark.parametrize("image,i,j,expected", [
    (np.array([[1]]), 0, 0, 1),  # Single pixel image
    (np.array([[1, 1], [1, 1]]), 1, 0, 0),  # 2x2 image of ones, x moment about centroid
    (np.array([[1, 1], [1, 1]]), 0, 1, 0),  # 2x2 image of ones, y moment about centroid
    (np.array([[1, 2], [3, 4]]), 1, 1, -0.2),  # Weighted sum considering both x and y powers
    (np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]), 2, 0, 2), # Moments considering both x and y powers, adjusted for the centroid
    (np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]), 0, 2, 2), # Moments considering both x and y powers, adjusted for the centroid
])
def test_central_moment(image, i, j, expected):
    result = central_moment(image, i, j)
    assert np.isclose(result, expected, atol=1e-6), f"Expected {expected}, but got {result}"


###################################################################################################
test_data_nm = [
    (np.array([[0, 0], [0, 0]]), 0, 0, 0.0),  # Edge case: all-zero image
    (np.array([[1, 1], [1, 1]]), 0, 0, 1.0),  # Uniform image, i+j < 2
    (np.array([[1, 1], [1, 1]]), 1, 0, 0.0),  # Uniform image, i+j < 2
    (np.array([[1, 1], [1, 1]]), 1, 1, 0.0),  # Uniform image, i+j >= 2
    (np.array([[1, 1], [1, 1]]), 2, 0, 0.0625),  # Uniform image, i+j >= 2
    (np.array([[0, 1], [0, 1]]), 1, 1, 0.0),  # Non-uniform image, i+j >= 2
    (np.array([[0, 1], [0, 1]]), 0, 1, 0.0),  # Non-uniform image, i+j < 2
    (np.array([[0, 1], [1, 0]]), 0, 1, 0.0),  # Non-uniform image with alternating 0s and 1s, i+j < 2
    (np.array([[0, 1], [1, 0]]), 1, 1, -0.125),  # Non-uniform image with alternating 0s and 1s, i+j >= 2
]
@pytest.mark.parametrize("image, i, j, expected", test_data_nm)
def test_normalized_moment(image, i, j, expected):
    result = normalized_moment(image, i, j)
    assert np.isclose(result, expected, atol=1e-6), f"Expected {expected}, but got {result}"


###################################################################################################

# Define some simple test images
all_zero = np.zeros((3, 3))
uniform = np.ones((3, 3))
rectangle = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
])
cross = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
])

# Define test data, where each tuple contains an image, the Hu moment index, and the expected value
test_data_hm = [
    (all_zero, 1, 0.0),  # Testing all-zero image should give 0 for all Hu moments
    (all_zero, 2, 0.0),
    (all_zero, 3, 0.0),
    (all_zero, 4, 0.0),
    (all_zero, 5, 0.0),
    (all_zero, 6, 0.0),
    (all_zero, 7, 0.0),
    (uniform, 1, 0.148148148),  # For uniform image, only the first Hu moment is non-zero
    (uniform, 2, 0.0),
    (rectangle, 1, 0.22222222),
    (rectangle, 2, 0.0493827),
    (rectangle, 3, 0.0),
    (rectangle, 4, 0.0),
    (cross, 1, 0.16),
    (cross, 2, 0.0),
]

@pytest.mark.parametrize("image, m, expected", test_data_hm)
def test_hu_moment(image, m, expected):
    result = hu_moment(image, m)
    assert np.isclose(result, expected, atol=1e-6), f"For m={m}, expected {expected}, but got {result}"