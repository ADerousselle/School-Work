import numpy as np
from central_moment import central_moment

def get_features_cm(image):
    """Calculate central moments for the passed image and return a feature vector."""
    fvector = np.zeros(8)

    fvector[0] = central_moment(image, 0, 0)
    fvector[1] = central_moment(image, 1, 1)
    fvector[2] = central_moment(image, 2, 0)
    fvector[3] = central_moment(image, 0, 2)
    fvector[4] = central_moment(image, 2, 1)
    fvector[5] = central_moment(image, 1, 2)
    fvector[6] = central_moment(image, 3, 0)
    fvector[7] = central_moment(image, 0, 3)
    
    return fvector
