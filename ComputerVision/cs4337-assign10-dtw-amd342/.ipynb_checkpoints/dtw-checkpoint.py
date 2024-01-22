import numpy as np

def dtw(sequence1, sequence2):
    """
    Compute the Dynamic Time Warping (DTW) distance between two sequences.

    Parameters:
    sequence1 (np.array): A 2D numpy array representing the first sequence.
    sequence2 (np.array): A 2D numpy array representing the second sequence.

    Returns:
    float: The DTW distance between the two sequences.
    """

    if (
        (len(sequence1[0]) == 0 or len(sequence2[0]) == 0)
        or
        (len(sequence1[0]) == 1 and len(sequence2[0]) == 1)
        or
        (np.array_equal(sequence1, sequence2))):
        return 0

    #Initialize distance matrix
    distance_M = np.zeros ((len(sequence1[0]), len(sequence2[0])))

    #Calculate distances between points in the sequence
    for i in range(len(sequence1[0])):
        for j in range(len(sequence2[0])):
            distance_M[i,j] = np.linalg.norm(sequence1[:, i] - sequence2[:,j])

    #Initialize the accumulated cost matrix
    accum_cost_M = np.zeros((len(sequence1[0]), len(sequence2[0])))
    accum_cost_M[0,0] = distance_M[0,0]

    #Calculate the accumulated cost matrix
    for i in range(1, len(sequence1[0])):
        accum_cost_M[i,0] = accum_cost_M[i-1, 0] + distance_M[i,0]
    for j in range(1, len(sequence2[0])):
        accum_cost_M[0,j] = accum_cost_M[0, j-1] + distance_M[0,j]

    for i in range(1, len(sequence1[0])):
        for j in range(1, len(sequence2[0])):
            accum_cost_M[i,j] = distance_M[i,j] + min(
                accum_cost_M[i-1, j],
                accum_cost_M[i, j-1],
                accum_cost_M[i-1, j-1]
            )
    dtw_dist = accum_cost_M[-1, -1]

    return dtw_dist