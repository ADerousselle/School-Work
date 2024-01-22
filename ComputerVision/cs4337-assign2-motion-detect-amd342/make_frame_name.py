def make_frame_name(dir_name, frame):
    """
    Creates a frame filename given the directory name and the frame name, 
    for frames of the walkstraight sequence.
    """
    
    if frame < 10:
        frame_filename = f"{dir_name}000{frame}.tif"
    elif frame < 100:
        frame_filename = f"{dir_name}00{frame}.tif"
    else:
        frame_filename = f"{dir_name}0{frame}.tif"
    
    return frame_filename
	
	
# Example usage
# dir_name = "walkstraight"
# frame = 5
# frame_filename = make_frame_name(dir_name, frame)
# print(frame_filename)