import cv2
import numpy as np
from draw_rectangle import draw_rectangle
import matplotlib.pyplot as plt

def chamfer_search(edge_image, template, scale, number_of_results):

    # Apply distance transform to the edge image
    edge_image_inv = cv2.bitwise_not(edge_image)
    distance_transform = cv2.distanceTransform(edge_image_inv, cv2.DIST_L2, 5)
    
    # Resize the template and convert to uint8
    resized_template = cv2.resize(template, None, fx=scale, fy=scale).astype(np.uint8)
    
    # Compute Chamfer distance scores
    convolution_scores = cv2.filter2D(distance_transform, -1, resized_template)
    
    # Normalize the result
    scores = convolution_scores / convolution_scores.max()
    scores_copy = scores.copy()
    
    # Find top matches without overlap
    top_matches = []
    for _ in range(number_of_results):
        # Find the minimum location in the current result
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(scores_copy)
        top_matches.append(min_loc)
    
        # Set the pixels within the region of the current match to 1
        y1 = min_loc[1] - int(resized_template.shape[0] / 2)
        y2 = min_loc[1] + int(resized_template.shape[0] / 2)
        x1 = min_loc[0] - int(resized_template.shape[1] / 2)
        x2 = min_loc[0] + int(resized_template.shape[1] / 2)
        scores_copy[y1:y2, x1:x2] = 1
    
    # Create result image and draw bounding rectangles
    result_image = cv2.imread('data/clutter1_edges.bmp')
    
    for (x, y) in top_matches:
        top = y + int(resized_template.shape[0] / 2)
        bottom = y - int(resized_template.shape[0] / 2)
        left = x - int(resized_template.shape[1] / 2)
        right = x + int(resized_template.shape[1] / 2)
        result_image = draw_rectangle(result_image, top, bottom, left, right)

    return scores, result_image
