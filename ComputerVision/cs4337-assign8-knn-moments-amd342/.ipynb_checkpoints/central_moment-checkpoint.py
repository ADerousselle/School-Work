import numpy as np
from raw_moment import raw_moment

def central_moment(image, i, j):
    """Compute the central moment."""
    M00 = raw_moment(image, i, j)
    M01 = raw_moment(image, 0, 1)
    M10 = raw_moment(image, 1, 0)
    x_bar = M10 / M00
    y_bar = M01 / M00

    central_moment = np.sum(((np.arange(image.shape[1]) - x_bar) ** i) * ((np.arange(image.shape[0]) - y_bar) ** j) * image)
    
    return central_moment
