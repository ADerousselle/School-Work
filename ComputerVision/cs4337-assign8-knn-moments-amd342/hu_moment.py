import numpy as np
from normalized_moment import normalized_moment

def hu_moment(image, m):
    """Compute the m-th Hu moment."""
    if np.sum(image) == 0:
        return 0.0
    else:
        if m == 1:
            m20 = normalized_moment(image, 2, 0)
            m02 = normalized_moment(image, 0, 2)
            hu_moment = (m20 + m02)
        elif m == 2:
            m20 = normalized_moment(image, 2, 0)
            m02 = normalized_moment(image, 0, 2)
            m11 = normalized_moment(image, 1, 1)
            hu_moment = ((m20 - m02)**2 + (2*m11)**2)
        elif m == 3:
            m30 = normalized_moment(image, 3, 0)
            m03 = normalized_moment(image, 0, 3)
            m12 = normalized_moment(image, 1, 2)
            m21 = normalized_moment(image, 2, 1)
            hu_moment = ((m30 - 3*m12)**2 + (3*m21 - m03)**2)
        elif m == 4:
            m30 = normalized_moment(image, 3, 0)
            m03 = normalized_moment(image, 0, 3)
            m12 = normalized_moment(image, 1, 2)
            m21 = normalized_moment(image, 2, 1)
            hu_moment = ((m30 + m12)**2 + (m21 + m03)**2)
        elif m == 5:
            m30 = normalized_moment(image, 3, 0)
            m03 = normalized_moment(image, 0, 3)
            m12 = normalized_moment(image, 1, 2)
            m21 = normalized_moment(image, 2, 1)
            hu_moment = ((m30 - 3*m12) * (m30 + m12) * ((m30 + m12)**2 - 3*(m21 + m03)**2) + (3*m21 - m03) * (m21 + m03)*(3*(m30 + m12)**2 - (m21 + m03)**2))
        elif m == 6:
            m20 = normalized_moment(image, 2, 0)
            m02 = normalized_moment(image, 0, 2)
            m30 = normalized_moment(image, 3, 0)
            m03 = normalized_moment(image, 0, 3)
            m12 = normalized_moment(image, 1, 2)
            m21 = normalized_moment(image, 2, 1)
            m11 = normalized_moment(image, 1, 1)
            hu_moment = ((m20 - m02) * ((m30 + m12)**2 - (m21 + m03)**2) + 4*m11 * (m30 + m12) * (m21 + m03))
        elif m == 7:
            m30 = normalized_moment(image, 3, 0)
            m03 = normalized_moment(image, 0, 3)
            m12 = normalized_moment(image, 1, 2)
            m21 = normalized_moment(image, 2, 1)
            hu_moment = ((3*m21 - m03) * (m30 + m12) * ((m30 + m12)**2 - 3*(m21 + m03)**2) - (m30 - 3*m12) * (m21 + m03) * (3*(m30 + m12)**2 - (m21 + m03)**2))

    return hu_moment