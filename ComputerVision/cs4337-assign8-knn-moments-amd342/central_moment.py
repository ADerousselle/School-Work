import numpy as np
from raw_moment import raw_moment

def central_moment(image, i, j):
    """Compute the central moment."""
    M00 = raw_moment(image, 0, 0)
    M01 = raw_moment(image, 0, 1)
    M10 = raw_moment(image, 1, 0)
    x_bar = M10 / M00
    y_bar = M01 / M00

    central_moment = 0.0
    for x in range(image.shape[0]):
        sum = 0.0
        for y in range(image.shape[1]):
            sum += ((x - x_bar) ** i) * ((y - y_bar) ** j) * image[x, y]
        central_moment += sum
    
    return central_moment
