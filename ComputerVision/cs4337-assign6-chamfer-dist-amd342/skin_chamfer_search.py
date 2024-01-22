import cv2
import numpy as np
import matplotlib.pyplot as plt
from draw_rectangle import draw_rectangle
from detect_skin import detect_skin
from chamfer_search import chamfer_search

def skin_chamfer_search(color_image, edge_image, template, scale, number_of_results):
    threshold = .05
    pos_hist = np.load('data/positive_histogram.npy')
    neg_hist = np.load('data/negative_histogram.npy')
    
    skin_mask = detect_skin(color_image, pos_hist, neg_hist)  # Load histograms using np.load()
    
    # Step 2: Apply skin mask to the edge image
    edge_image_skin = edge_image.copy()
    edge_image_skin[skin_mask < threshold] = 0
    
    
    # Step 3: Use chamfer search in the skin-filtered edge image
    scores, result_image = chamfer_search(edge_image_skin, template, scale, number_of_results)
    
    # Step 4: Return the top match's score and resulting image
    top_score = scores[0]

    return scores, result_image
