import numpy as np

def raw_moment(image, i, j):
    """Computes the raw moment M_ij for a grayscale image."""
    r, c = image.shape
    
    # Slow but simple implementation using loops
    # M = 0
    # for x in range(r):
    #     for y in range(c):
    #         M += (x**i) * (y**j) * image[x, y]

    # Faster implementation using NumPy
    x, y = np.meshgrid(np.arange(r), np.arange(c), indexing='ij')
    M = np.sum((x**i) * (y**j) * image)

    return M
