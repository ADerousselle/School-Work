import numpy as np
from dtw import dtw
from dtw2 import dtw2

def main():
    # Sample inputs for dtw.py
    seq1a = np.array([[0.30, 0.40, 0.50, 0.60, 0.50, 0.40, 0.30, 0.40, 0.50, 0.60],
                    [0.80, 0.90, 0.90, 0.80, 0.60, 0.50, 0.40, 0.40, 0.40, 0.40]])

    seq2a = np.array([[0.29, 0.36, 0.46, 0.58, 0.53, 0.46, 0.36, 0.29, 0.43, 0.54, 0.59, 0.6077],
                    [0.80, 0.89, 0.89, 0.81, 0.66, 0.57, 0.47, 0.40, 0.40, 0.40, 0.42, 0.4299]])

    seq1b = np.array([[0.10, 0.17, 0.24, 0.31, 0.36, 0.40, 0.42, 0.46, 0.50, 0.57, 0.64, 0.71, 0.74, 0.77, 0.81, 0.83, 0.86, 0.90, 0.95, 0.99],
                    [0.30, 0.38, 0.49, 0.54, 0.54, 0.47, 0.37, 0.29, 0.25, 0.26, 0.26, 0.26, 0.31, 0.38, 0.38, 0.32, 0.25, 0.25, 0.24, 0.25]])

    seq2b = np.array([[0.13, 0.18, 0.21, 0.25, 0.29, 0.32, 0.38, 0.42, 0.42, 0.45, 0.47, 0.51, 0.56, 0.63, 0.67, 0.72, 0.74, 0.77, 0.79, 0.81, 0.83, 0.87, 0.92, 0.97],
                    [0.29, 0.31, 0.32, 0.38, 0.47, 0.52, 0.54, 0.52, 0.46, 0.37, 0.32, 0.28, 0.26, 0.26, 0.26, 0.35, 0.38, 0.38, 0.34, 0.28, 0.25, 0.25, 0.26, 0.24]])

    result_a = dtw(seq1a, seq2a)
    result_b = dtw(seq1b, seq2b)

    print("\nDTW distance between seq1a and seq2a: {}".format(result_a))
    print("\nDTW distance between seq1b and seq2b: {}".format(result_b))

    # Sample inputs for dtw2.py
    seq1c = np.array([[0.69, 0.72, 0.72, 0.76, 0.81, 0.82, 0.84, 0.87],
                  [0.26, 0.26, 0.30, 0.38, 0.38, 0.30, 0.26, 0.25]])

    seq2c = np.array([[0.10, 0.17, 0.24, 0.31, 0.36, 0.40, 0.42, 0.46, 0.50, 0.57, 0.64, 0.71, 0.74, 0.77, 0.81, 0.83, 0.86, 0.90, 0.95, 0.99],
                    [0.30, 0.38, 0.49, 0.54, 0.54, 0.47, 0.37, 0.29, 0.25, 0.26, 0.26, 0.26, 0.31, 0.38, 0.38, 0.32, 0.25, 0.25, 0.24, 0.25]])

    # Compute the DTW distance and find start and end frames
    result_c, start_frame_c, end_frame_c = dtw2(seq1c, seq2c)

    print("\nDTW distance between seq1c and seq2c: {}".format(result_c))
    print("Start frame of seq2c: {}".format(start_frame_c))
    print("End frame of seq2c: {}".format(end_frame_c))



if __name__ == '__main__':
    main()