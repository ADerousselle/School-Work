from central_moment import central_moment
from raw_moment import raw_moment
import numpy as np

def normalized_moment(image, i, j):
    """Compute the normalized central moment."""
    if np.sum(image) == 0:
        return 0.0
    Cmoment = central_moment(image, i ,j)
    norm_Cmoment = Cmoment/(raw_moment(image, 0, 0)**(1 + (i+j)/2))
    return norm_Cmoment
