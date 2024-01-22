import cv2 as cv
import numpy as np
from find_bounding_box import find_bounding_box

def main():
    # Read frames in grayscale
    frame_path = "walkstraight/frame0052.tif"
    top_row, bottom_row, left_column, right_column = find_bounding_box(frame_path)

    print("Top row: ", top_row)
    print("Bottom row: ", bottom_row)
    print("Left column: ", left_column)
    print("Right column: ", right_column)


if __name__ == "__main__":
    main()