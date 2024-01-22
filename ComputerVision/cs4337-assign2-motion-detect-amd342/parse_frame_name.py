def parse_frame_name(frame_filename):
    """
    A hack that can separate the directory name from the frame name for 
    filenames of image files of the walkstraight sequence.
    """
    
    length = len(frame_filename)
    dir_name = frame_filename[:length-8]
    frame_string = frame_filename[length-7:length-4]
    frame = int(frame_string)
    
    return dir_name, frame
	
	
# Example usage
# frame_filename = "walkstraight/frame0005.tif"
# dir_name, frame = parse_frame_name(frame_filename)
# print(f"Directory name: {dir_name}")
# print(f"Frame: {frame}")