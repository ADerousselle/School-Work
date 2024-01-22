import numpy as np

import numpy as np

def build_histograms(data):
    """
    Builds skin and non-skin color histograms from a given dataset file.

    Args:
    - data (numpy.ndarray): The dataset array with shape (N, 4). Each row represents a pixel, and the 
                            columns represent the B, G, R values and the label (1 for skin, 2 for non-skin).

    Returns:
    - skin_histogram (numpy.ndarray): A 3D numpy array representing the skin color histogram.
    - nonskin_histogram (numpy.ndarray): A 3D numpy array representing the non-skin color histogram.
    """
 
    # Your code here...
            
    return skin_histogram, nonskin_histogram