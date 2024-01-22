[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/AQeFE1Zk)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=11737294)
# CS 4337 - Assignment 2 - Motion Detection
To complete the assignment, you will need to implement the function `find_bounding_box.py`. The function should take in the path to a frame and use other frames in the same directory to find the bounding box of the moving object using frame differencing. The function should return the bounding box as a tuple of the form `(top_row, bottom_row, left_column, right_column)`. The function should also save the binarized frame with the bounding box drawn in yellow on it in the `output` folder.

## File list

This repository contains the following files and folders:

- `README.md`: This file.
- `.gitignore`: This file tells git which files to ignore.
- `find_bounding_box.py`: This is the file you will need to complete.
- `tests/test_find_bounding_box.py`: This file contains the unit tests for the `find_bounding_box.py` file.
- `parse_frame_name.py`: This file is used to parse the frame names in the `walkstraight` folder and extract the frame number.
- `make_frame_number.py`: This file is used to generate the frame names when given a directory and a frame number.
- `read_gray.py`: This file is used to read a frame and convert it to grayscale.
- `requirements.txt`: This file contains the list of Python packages required to run the code in this repository.
- `walkstraight`: This folder contains the sequence of frames used for testing.
- `output`: This folder is where the output of the `find_bounding_box.py` file will be stored. A sample output is provided.
- `.github/workflows`: This folder contains the GitHub Actions workflow file that is used to run the unit tests on every commit.


## Setting up the environment

If you are running the code on your own machine, and you followed the tutorial posted on Canvas for setting up your environment for running computer vision applications, your environment should be ready to run the code. If you use Github Codespaces the environment will need to be set up by installing the packages listed in the `requirements.txt` file. You can do this by running the following command in the terminal:

```bash
pip install -r requirements.txt
```

**Note:** If on Github Codespaces after installing the required packages you get the error `ImportError: libGL.so.1: cannot open shared object file: No such file or directory`, you will need to run the following command in the terminal:

```bash
sudo apt-get update && sudo apt-get install -y libgl1-mesa-glx
```

## Running the code

To test your function, you will need to run the `main.py` file which calls the `find_bounding_box.py` function. You can modify the `main.py` file to test your function on different frames. You can do this by running the following command:

```bash
python main.py
```
## Running the tests

To run the unit tests, you will need to run the following command:

```bash
pytest
```
Your function should pass all the tests in the `tests/test_find_bounding_box.py` file. If it does not, you will need to modify your function until it does.