import cv2
import numpy as np
import matplotlib.pyplot as plt
from get_component import get_component
from remove_holes import remove_holes

def detect_players(image_path):
    """
    Detects the positions of red and blue players in a soccer field image.

    Args:
        image_path (str): The path to the input image file.

    Returns:
        Tuple of five elements:
        - red_player_centroids (List[Tuple[int, int]]): The (x, y) coordinates of the centroids of the detected red players.
        - blue_player_centroids (List[Tuple[int, int]]): The (x, y) coordinates of the centroids of the detected blue players.
        - field (np.ndarray): The binary image of the soccer field.
        - red_players (np.ndarray): The binary image of the detected red players.
        - blue_players (np.ndarray): The binary image of the detected blue players.
    """
    
    # Load the image
    image = cv2.imread(image_path)

    #Blur to reduce noise
    image = cv2.medianBlur(image, 1)
    
    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.astype(np.float32)

    #Split the image into red, green, and blue channels
    r, g, b = cv2.split(image)
    
    # Find regions where each color is dominant
    blue = (b - g > 5) & (b - r > 5)
    green = (g - b > 10) & (g - r > 10)
    red = (r - g > 10) & (r - b > 10)
        
    # Convert boolean to binary (0 or 255)
    blue = blue.astype(np.uint8) * 255
    green = green.astype(np.uint8) * 255
    red = red.astype(np.uint8) * 255
        
    # Dilate the color regions
    kernel = np.ones((3,3), np.uint8)
    blue = cv2.dilate(blue, kernel)
    green = cv2.dilate(green, kernel)
    
    #Open and Close field region
    kernel = np.ones((9,9), np.uint8)
    field = cv2.morphologyEx(green, cv2.MORPH_OPEN, kernel)
    field = cv2.morphologyEx(field, cv2.MORPH_CLOSE, kernel)
    
    #Pick out people in blue/red on the field
    kernel = np.ones((5,5), np.uint8)
    blue_players = (field & blue)
    blue_players = cv2.morphologyEx(blue_players, cv2.MORPH_OPEN, kernel)
    blue_players = cv2.morphologyEx(blue_players, cv2.MORPH_CLOSE, kernel)
    red_players = (field & red)
    red_players = cv2.morphologyEx(red_players, cv2.MORPH_OPEN, kernel)
    red_players = cv2.morphologyEx(red_players, cv2.MORPH_CLOSE, kernel)

    #Get the centroid locations for the red and blue players, and remove the background centroid from the list of centroids
    b_num_labels, labels, stats, blue_player_centroids = cv2.connectedComponentsWithStats(blue_players, connectivity=4)
    blue_player_centroids = blue_player_centroids[1:]
    r_num_labels, r_labels, stats, red_player_centroids = cv2.connectedComponentsWithStats(red_players, connectivity=4)
    red_player_centroids = red_player_centroids[1:]

    #Organize the centroids in ascending order
    blue_player_centroids = sorted(blue_player_centroids, key=lambda centroid: centroid[0])
    red_player_centroids = sorted(red_player_centroids, key=lambda centroid: centroid[0])

    return red_player_centroids, blue_player_centroids, field, red_players, blue_players

