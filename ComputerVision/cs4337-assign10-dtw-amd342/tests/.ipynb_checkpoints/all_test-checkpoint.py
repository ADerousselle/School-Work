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
from dtw import dtw
from dtw2 import dtw2

def test_dtw_with_empty_sequences():
    seq1 = np.array([[], []])
    seq2 = np.array([[], []])
    assert dtw(seq1, seq2) == 0, "DTW distance should be 0 for empty sequences"

def test_dtw_with_single_point_sequences():
    seq1 = np.array([[1], [2]])
    seq2 = np.array([[1], [2]])
    assert dtw(seq1, seq2) == 0, "DTW distance should be 0 for identical single-point sequences"

def test_dtw_with_identical_sequences():
    seq1 = np.array([[1, 2, 3], [2, 3, 4]])
    seq2 = np.array([[1, 2, 3], [2, 3, 4]])
    assert dtw(seq1, seq2) == 0, "DTW distance should be 0 for identical sequences"

def test_dtw_with_different_length_sequences():
    seq1 = np.array([[1, 2], [2, 3]])
    seq2 = np.array([[1, 2, 3], [2, 3, 4]])
    assert dtw(seq1, seq2) >= 0, "DTW distance should be non-negative"

def test_dtw_with_known_distance():
    seq1 = np.array([[0, 1], [0, 1]])
    seq2 = np.array([[1, 2], [1, 2]])
    # The expected DTW distance should be calculated manually for these sequences
    expected_distance = 2.8284271247461903  # Example value, replace with the correct one
    assert dtw(seq1, seq2) == pytest.approx(expected_distance), "DTW distance should match the known value"

def test_dtw_with_sample_input_a():
    # Sample inputs for dtw.py
    seq1a = np.array([[0.30, 0.40, 0.50, 0.60, 0.50, 0.40, 0.30, 0.40, 0.50, 0.60],
                    [0.80, 0.90, 0.90, 0.80, 0.60, 0.50, 0.40, 0.40, 0.40, 0.40]])

    seq2a = np.array([[0.29, 0.36, 0.46, 0.58, 0.53, 0.46, 0.36, 0.29, 0.43, 0.54, 0.59, 0.6077],
                    [0.80, 0.89, 0.89, 0.81, 0.66, 0.57, 0.47, 0.40, 0.40, 0.40, 0.42, 0.4299]])

    result_a = dtw(seq1a, seq2a)

    # result_a should be 0.4151 with a tolerance of 0.0001
    assert abs(result_a - 0.4151) < 0.0001

def test_dtw_with_sample_input_b():
    seq1b = np.array([[0.10, 0.17, 0.24, 0.31, 0.36, 0.40, 0.42, 0.46, 0.50, 0.57, 0.64, 0.71, 0.74, 0.77, 0.81, 0.83, 0.86, 0.90, 0.95, 0.99],
                    [0.30, 0.38, 0.49, 0.54, 0.54, 0.47, 0.37, 0.29, 0.25, 0.26, 0.26, 0.26, 0.31, 0.38, 0.38, 0.32, 0.25, 0.25, 0.24, 0.25]])

    seq2b = np.array([[0.13, 0.18, 0.21, 0.25, 0.29, 0.32, 0.38, 0.42, 0.42, 0.45, 0.47, 0.51, 0.56, 0.63, 0.67, 0.72, 0.74, 0.77, 0.79, 0.81, 0.83, 0.87, 0.92, 0.97],
                    [0.29, 0.31, 0.32, 0.38, 0.47, 0.52, 0.54, 0.52, 0.46, 0.37, 0.32, 0.28, 0.26, 0.26, 0.26, 0.35, 0.38, 0.38, 0.34, 0.28, 0.25, 0.25, 0.26, 0.24]])

    result_b = dtw(seq1b, seq2b)

    # result_b should be 0.8490 with a tolerance of 0.0001
    assert abs(result_b - 0.8490) < 0.0001



def test_dtw2_with_simple_sequences():
    seq1 = np.array([[1, 2, 3], [2, 3, 4]])
    seq2 = np.array([[1, 2, 3, 4], [2, 3, 4, 5]])
    result, start_frame, end_frame = dtw2(seq1, seq2)
    assert result >= 0, "DTW distance should be non-negative"
    assert 0 <= start_frame <= end_frame < seq2.shape[1], "Start and end frames should be within sequence bounds"

def test_dtw2_with_empty_sequences():
    seq1 = np.array([[], []])
    seq2 = np.array([[], []])
    result, start_frame, end_frame = dtw2(seq1, seq2)
    assert result == 0, "DTW distance for empty sequences should be 0"
    assert start_frame == end_frame == 0, "Start and end frames should be 0 for empty sequences"

def test_dtw2_with_identical_sequences():
    seq1 = np.array([[1, 2, 3], [2, 3, 4]])
    result, start_frame, end_frame = dtw2(seq1, seq1)
    assert result == 0, "DTW distance should be zero for identical sequences"
    assert start_frame == 0 and end_frame == seq1.shape[1] - 1, "Start and end frames should encompass the entire sequence for identical sequences"

def test_dtw2_with_different_length_sequences():
    seq1 = np.array([[1, 2], [2, 3]])
    seq2 = np.array([[1, 2, 3], [2, 3, 4]])
    result, start_frame, end_frame = dtw2(seq1, seq2)
    assert result >= 0, "DTW distance should be non-negative"
    assert 0 <= start_frame <= end_frame < seq2.shape[1], "Start and end frames should be within sequence bounds"

def test_dtw2_sample_input_c():
    seq1c = np.array([[0.69, 0.72, 0.72, 0.76, 0.81, 0.82, 0.84, 0.87],
                  [0.26, 0.26, 0.30, 0.38, 0.38, 0.30, 0.26, 0.25]])

    seq2c = np.array([[0.10, 0.17, 0.24, 0.31, 0.36, 0.40, 0.42, 0.46, 0.50, 0.57, 0.64, 0.71, 0.74, 0.77, 0.81, 0.83, 0.86, 0.90, 0.95, 0.99],
                    [0.30, 0.38, 0.49, 0.54, 0.54, 0.47, 0.37, 0.29, 0.25, 0.26, 0.26, 0.26, 0.31, 0.38, 0.38, 0.32, 0.25, 0.25, 0.24, 0.25]])

    # Compute the DTW distance and find start and end frames
    result_c, start_frame_c, end_frame_c = dtw2(seq1c, seq2c)

    # result_c should be 0.1171, start_frame = 11, end_frame = 16
    assert abs(result_c - 0.1171) < 0.0001
    assert start_frame_c == 11
    assert end_frame_c == 16

