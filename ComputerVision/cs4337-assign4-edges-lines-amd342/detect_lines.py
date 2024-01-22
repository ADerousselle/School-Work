import cv2 as cv
import numpy as np

def detect_lines(img, sigma, threshold, numLines):
    """
    Detects lines in a color or grayscale image using the a custom implementation of the Hough transform.

    Parameters:
    img (numpy.ndarray): The input image.
    sigma (float): The standard deviation of the Gaussian blur applied to the image.
    threshold (int): The low threshold value used for Canny edge detection. The high threshold is twice this value.
    numLines (int): The maximum number of lines to detect.

    Returns:
    list: A list of tuples representing the detected lines. Each tuple contains
        two values: rho and theta, where rho is the distance from the origin to
        the line and theta is the angle between the x-axis and the normal to the line.
    """

    #Reduce noise and get an image of just the edges of the original image from Canny.
    img_blur = cv.GaussianBlur(img, (0,0), sigma)
    canny = cv.Canny(img_blur, threshold, 2*threshold)
    #Get the rows, columns, and furthest distance from the origin.
    rows, cols = canny.shape
    max_rho = int(np.sqrt(rows**2 + cols**2))
    #Create a vote accumulator for voting on lines
    accumulator = np.zeros((2 * max_rho, 180), dtype=np.uint32)


    #Vote for lines, store votes in the accumulator
    #For every pixel
    for y in range(rows):
        for x in range(cols):
            if canny[y, x] == 255:
                #For each possible theta 
                for theta in range(0, 180):
                    #calculate the rho for that theta and pixel
                    rho = int(x * np.cos(np.deg2rad(theta)) + y * np.sin(np.deg2rad(theta))) + max_rho
                    #increment the accumulator at index [rho, theta] to place a vote for which line the pixel should be part of
                    accumulator[rho, theta] += 1

    #Find the top numLines lines with the most votes
    lines = []
    #Loop to find the expected number of lines.
    for line in range(numLines):
        #If there are no more lines with votes break from the loop
        max_vote = np.max(accumulator)
        if max_vote == 0:
            break
        #Get the index of the current max votes
        rho_idx, theta_idx = np.unravel_index(np.argmax(accumulator), accumulator.shape)
        #Get rho and theta and add it to the list of lines that will be returned
        rho = rho_idx - max_rho
        theta = theta_idx
        lines.append((rho, theta))
        #set that line's votes to 0 so that it is not recounted
        accumulator[rho_idx, theta_idx] = 0

    return lines