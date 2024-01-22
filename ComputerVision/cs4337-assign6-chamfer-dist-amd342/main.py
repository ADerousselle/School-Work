#%% Import libraries and read data
import cv2
import numpy as np
import matplotlib.pyplot as plt
from chamfer_search import chamfer_search
from skin_chamfer_search import skin_chamfer_search

# Read the images
color_image = cv2.imread('data/clutter1.bmp')
color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

edge_image = cv2.imread('data/clutter1_edges.bmp', cv2.IMREAD_GRAYSCALE)
template = cv2.imread('data/template.bmp', cv2.IMREAD_GRAYSCALE)


#%% Test chamfer_search

# Run for scale 1
scale = 1
number_of_results = 5

scores, result_image = chamfer_search(edge_image, template, scale, number_of_results)


plt.figure()
plt.imshow(result_image, cmap='gray')
plt.show()

#%% Test chamfer_search for scale 1.5
# Resize the image and run for scale 1.5
edge_image_scaled = cv2.resize(edge_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
# Convert to binary image
edge_image_scaled = (edge_image_scaled > 0).astype(np.uint8)*255

scale = 1.5
number_of_results = 5

scores, result_image = chamfer_search(edge_image_scaled, template, scale, number_of_results)

plt.figure()
plt.imshow(result_image, cmap='gray')
plt.show()


#%% Test skin_chamfer_search for scale 1

# Run for scale 1
scale = 1
number_of_results = 1

scores, result_image = skin_chamfer_search(color_image, edge_image, template, scale, number_of_results)

plt.figure()
plt.imshow(result_image, cmap='gray')
plt.show()

# Print the minimum distance score in the scores array and the corresponding row and column
min_score = np.min(scores)
row, col = np.unravel_index(np.argmin(scores, axis=None), scores.shape)
print(f"Minimum score: {min_score:.4f}")
print(f"Row: {row}, Column: {col}")

# %% Test skin_chamfer_search for scale 1.5

# Resize the image and run for scale 1.5
color_image_scaled = cv2.resize(color_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
edge_image_scaled = cv2.resize(edge_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
# Convert to binary image
edge_image_scaled = (edge_image_scaled > 0).astype(np.uint8)*255

scale = 1.5
number_of_results = 1

scores, result_image = skin_chamfer_search(color_image_scaled, edge_image_scaled, template, scale, number_of_results)

plt.figure()
plt.imshow(result_image, cmap='gray')
plt.show()

# Print the minimum distance score in the scores array and the corresponding row and column
min_score = np.min(scores)
row, col = np.unravel_index(np.argmin(scores, axis=None), scores.shape)
print(f"Minimum score: {min_score:.4f}")
print(f"Row: {row}, Column: {col}")
