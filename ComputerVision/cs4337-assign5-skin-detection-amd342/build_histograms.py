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
 
    #Initialize skin and nonskin histograms
    skin_histogram = np.zeros((32, 32, 32), dtype = np.float64)
    nonskin_histogram = np.zeros((32, 32, 32),dtype = np.float64)
    
    #Iterate over the pixels in the dataset
    for pxl in data:
        #Extract values
        b, g, r, l = pxl
        #Calculate the bins indices for each channel
        bin_r = int(r * 32 / 256)
        bin_g = int(g * 32 / 256)
        bin_b = int(b * 32 / 256)
        # Normalize pixel values to the range [0, 1]
        normalized_pixel = np.array(pxl) / 255.0
        #Update the l histogram 
        if l == 1:
            skin_histogram[bin_r, bin_g, bin_b] += 1
        elif l == 2:
            nonskin_histogram[bin_r, bin_g, bin_b] += 1
    
    # Calculate the total number |of skin and non-skin pixels
    total_skin_pixels = np.sum(skin_histogram)
    total_nonskin_pixels = np.sum(nonskin_histogram)
    
    # Normalize the histograms
    if total_skin_pixels > 0:
        skin_histogram /= total_skin_pixels
    if total_nonskin_pixels > 0:
        nonskin_histogram /= total_nonskin_pixels
            
    return skin_histogram, nonskin_histogram