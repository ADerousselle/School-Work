import numpy as np

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return np.sqrt(np.sum((point1 - point2) ** 2))

def dtw2(sequence1, sequence2):
    """
    Compute the Dynamic Time Warping (DTW) distance between sequence1 and the best matching subsequence in sequence2.
    Also find the start and end frame of this subsequence in sequence2.

    Parameters:
    sequence1 (np.array): A 2D numpy array representing the first sequence.
    sequence2 (np.array): A 2D numpy array representing the second sequence.

    Returns:
    float: The DTW distance between the two sequences.
    int: The start frame of the best matching subsequence in sequence2.
    int: The end frame of the best matching subsequence in sequence2.
    """
    
    if (len(sequence1[0]) == 0 or len(sequence2[0]) == 0) or (len(sequence1[0]) == 1 and len(sequence2[0]) == 1):
        return 0, 0, 0
   
    if np.array_equal(sequence1, sequence2):
        return 0, 0, len(sequence2[0]) - 1
    
    #Initialize distance matrix
    distance_M = np.zeros ((len(sequence1[0]), len(sequence2[0])))

    #Calculate distances between points in the sequence
    for i in range(len(sequence1[0])):
        for j in range(len(sequence2[0])):
            distance_M[i, j] = euclidean_distance(sequence1[:, i], sequence2[:, j])

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
    #Find end frame
    end = np.argmin(accum_cost_M[-1, :])

    #Find start frame
    start = end
    k = len(sequence1[0]) - 1
    while k > 0:
        if end == 0:
            start = 0;
        elif end == len(sequence2[0]) - 1:
            start = len(sequence1[0]) - 1
        else:
            prev_col = [end - 1, end, end + 1]
            min_idx = np.argmin(accum_cost_M[k-1, prev_col])
            start = start + min_idx -1
        k -= 1
    
    dtw_dist = accum_cost_M[-1, end+1] - accum_cost_M[0, start]
    
    return dtw_dist, start+1, end