import numpy as np
from get_features_cm import get_features_cm

def knn_classify_digit_cm(digit, K, train_cmoments_db):
    ''' Classify a digit using the KNN classifier based on central moments. '''
    train_cmoments, train_labels, min_vals, max_vals = train_cmoments_db

    # 1. Compute central moments for the query digit.
    query_cmoments = get_features_cm(digit)

    # 2. Normalize each moment to the range [0, 1].
    normalized_query_cmoments = (query_cmoments - min_vals) / (max_vals - min_vals)

    # 3. Compute the Euclidean distance between the query vector and all vectors in the database.
    distances = np.sqrt(np.sum((train_cmoments - normalized_query_cmoments) ** 2, axis=1))

    # 4. Find the top K nearest neighbors.
    nearest_indices = np.argpartition(distances, K)[:K]
    
    # 5. Assign the predicted label of the digit to be that of the majority of its top K neighbors.
    nearest_labels = train_labels[nearest_indices]
    nearest_labels = nearest_labels.astype(int)
    prediction = np.argmax(np.bincount(nearest_labels))
    
    return prediction