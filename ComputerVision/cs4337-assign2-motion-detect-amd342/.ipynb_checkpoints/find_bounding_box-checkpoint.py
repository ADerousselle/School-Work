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

    # TODO: Complete the function...




    # Save the motion image with the bounding box as a file
    cv.imwrite('output/detection_frame'+str(frame_number)+'.jpg', frame)
    
    return (top_row, bottom_row, left_column, right_column)
