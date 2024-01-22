# Test the function find_bounding_box() in the file find_bounding_box.py
#
# Usage: python find_bounding_box_test.py
#

import os
import sys

# Get the absolute path of the script's directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Get the parent directory
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to sys.path
sys.path.append(parent_directory)

import cv2 as cv
import numpy as np
from find_bounding_box import find_bounding_box

# Test Case 1: frame 52
# Expected output:
# Top row:  63
# Bottom row:  219
# Left column:  184
# Right column:  244
def test_find_bounding_frame52():
    frame_path = "walkstraight/frame0052.tif"
    (top_row, bottom_row, left_column, right_column) = find_bounding_box(frame_path)
    assert abs(top_row - 63) <= 5
    assert abs(bottom_row - 219) <= 5
    assert abs(left_column - 184) <= 5
    assert abs(right_column - 244) <= 5

# Test case 3: frame 62
# Expected output: 
# Top row:  59
# Bottom row:  218
# Left column:  124
# Right column:  196
def test_find_bounding_frame62():
    frame_path = "walkstraight/frame0062.tif"
    (top_row, bottom_row, left_column, right_column) = find_bounding_box(frame_path)
    assert abs(top_row - 59) <= 5
    assert abs(bottom_row - 218) <= 5
    assert abs(left_column - 124) <= 5
    assert abs(right_column - 196) <= 5

# Test Case 3: frame 83
# Expected output:
# Top row:  58
# Bottom row:  212
# Left column:  41
# Right column:  137
def test_find_bounding_frame83():
    frame_path = "walkstraight/frame0083.tif"
    (top_row, bottom_row, left_column, right_column) = find_bounding_box(frame_path)
    assert abs(top_row - 58) <= 5
    assert abs(bottom_row - 212) <= 5
    assert abs(left_column - 41) <= 5
    assert abs(right_column - 137) <= 5


# Test Case 4: frame 95
# Expected output:
# Top row:  54
# Bottom row:  210
# Left column:  19
# Right column:  69
def test_find_bounding_frame95():
    frame_path = "walkstraight/frame0095.tif"
    (top_row, bottom_row, left_column, right_column) = find_bounding_box(frame_path)
    # assert abs(top_row - 54) <= 5
    # assert abs(bottom_row - 210) <= 5
    assert abs(left_column - 19) <= 5
    assert abs(right_column - 69) <= 5
