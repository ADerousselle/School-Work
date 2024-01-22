
#%%

import cv2
import numpy as np
import matplotlib.pyplot as plt

from build_histograms import build_histograms
from detect_skin import detect_skin
from evaluate_histograms import evaluate_histograms


#%%

data = np.loadtxt("data/UCI_Skin_NonSkin.txt")
skin_hist_rgb, nonskin_hist_rgb = build_histograms(data)

#%%
# Load the image
image = cv2.imread("data/Face_Dataset/Pratheepan_Dataset/FacePhoto/Matthew_narrowweb__300x381,0.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

detection = detect_skin(image_rgb, skin_hist_rgb, nonskin_hist_rgb)


skin_mask = detection > 0.5

# Display the original image and the skin detection result
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image_rgb)
axes[0].axis('off')
axes[0].set_title("Original Image")
axes[1].imshow(skin_mask, cmap="gray")
axes[1].axis('off')
axes[1].set_title("Skin Detection Result")
plt.tight_layout()
plt.show()


#%%

accuracy_hist, TP, TN, FP, FN = evaluate_histograms(data, skin_hist_rgb, nonskin_hist_rgb, threshold=0.5)
print("Accuracy New Histogram: {:.2f}%".format(accuracy_hist * 100))
print("True Positives: {}".format(TP))
print("True Negatives: {}".format(TN))
print("False Positives: {}".format(FP))
print("False Negatives: {}".format(FN))


# %%

# Read histograms
negative_histogram = np.load('data/negative_histogram.npy')
positive_histogram = np.load('data/positive_histogram.npy')

accuracy_hist, TP, TN, FP, FN = evaluate_histograms(data, positive_histogram, negative_histogram, threshold=0.5)
print("Accuracy Old Histogram: {:.2f}%".format(accuracy_hist * 100))
print("True Positives: {}".format(TP))
print("True Negatives: {}".format(TN))
print("False Positives: {}".format(FP))
print("False Negatives: {}".format(FN))

detection = detect_skin(image_rgb, positive_histogram, negative_histogram)


skin_mask = detection > 0.5

# Display the original image and the skin detection result
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image_rgb)
axes[0].axis('off')
axes[0].set_title("Original Image")
axes[1].imshow(skin_mask, cmap="gray")
axes[1].axis('off')
axes[1].set_title("Skin Detection Result")
plt.tight_layout()
plt.show()