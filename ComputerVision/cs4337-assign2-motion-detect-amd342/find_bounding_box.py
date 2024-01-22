import cv2 as cv
import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from parse_frame_name import parse_frame_name
from make_frame_name import make_frame_name
from read_gray import read_gray

def find_bounding_box(frame_path):
    MIN_FRAME = 0
    MAX_FRAME = 124

    # Parse frame name
    dir_name, frame_number = parse_frame_name(frame_path)

    #Get paths and images of the needed files
    rgb_frame = cv.imread(frame_path)
    pre_file = make_frame_name(dir_name, frame_number-10)
    pre_frame = cv.imread(pre_file)
    post_file = make_frame_name(dir_name, frame_number+10)
    post_frame = cv.imread(post_file)

    #Convert each img to grayscale
    frame = cv.cvtColor(rgb_frame, cv.COLOR_BGR2GRAY)
    pre_frame = cv.cvtColor(pre_frame, cv.COLOR_BGR2GRAY)
    post_frame = cv.cvtColor(post_frame, cv.COLOR_BGR2GRAY)

    #Find the absolute difference between pre_frame and frame, and post_frame and frame
    pre_diff = cv.absdiff(frame, pre_frame)
    post_diff = cv.absdiff(frame, post_frame)

    #Find the motion of frame by taking the minimum of pre_diff and post_diff
    motion = cv.min(pre_diff, post_diff)

    #Use threshold() to create the binary image of the motion image
    thresh, binary_img = cv.threshold(motion, thresh = 10, maxval = 255, type = cv.THRESH_BINARY)

    #Find the connected components
    nb_components, output, stats, centroids = cv.connectedComponentsWithStats(binary_img, connectivity=8)

    #Find the largest non background component.
    max_label, max_size = max([(i, stats[i, cv.CC_STAT_AREA]) for i in range(1, nb_components)], key=lambda x: x[1])

    #Keep only the largest component.
    binary_img[output != max_label] = 0

    #Get the bounding box around the largest component
    left = int(stats[max_label, cv.CC_STAT_LEFT])
    top = int(stats[max_label, cv.CC_STAT_TOP])
    width = int(stats[max_label, cv.CC_STAT_WIDTH])
    height = int(stats[max_label, cv.CC_STAT_HEIGHT])

    bgr_binary_img = cv.cvtColor(binary_img, cv.COLOR_GRAY2BGR)
    
    # Draw the bounding box as a yellow rectangle
    cv.rectangle(bgr_binary_img, (left, top), (left+width, top+height), (0,255,255), 2)

    # Save the motion image with the bounding box as a file
    cv.imwrite('output/detection_frame'+str(frame_number)+'.jpg', bgr_binary_img)

    #Get rows and columns of bound box
    top_row = top
    bottom_row = top+height
    left_column = left
    right_column = left+width
    
    return (top_row, bottom_row, left_column, right_column)
