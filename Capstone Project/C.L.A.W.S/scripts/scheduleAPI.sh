#!/bin/bash

# Store the custom path in a different variable, not to overwrite the system PATH
PROJECT_PATH="/home/workspace/Software-Engineering-Project-Course"

NODE_EXECUTABLE="/usr/local/bin/node"  # Replace with actual path
PYTHON_EXECUTABLE="/usr/bin/python3"  # Replace with actual path

# Function to process JSON files and insert them into the database
process_json_files() {
    local JSON_FILES_DIRECTORY="${PROJECT_PATH}/scripts/json_files/*"
    cd "${PROJECT_PATH}/scripts/database_scripts"
    
    # Loop through all JSON files in the directory
    for json_file in $JSON_FILES_DIRECTORY; do
        # Check if the file exists and is not a directory
        if [ -f "$json_file" ]; then
            # Call the Node script with each JSON file
            $NODE_EXECUTABLE "Insert_Product_to_DB.js" "$json_file"
        fi
    done

    # Go to the directory and remove all JSON files
    cd "${PROJECT_PATH}/scripts/json_files"
    rm -f *.json
}

# Execute Python and Node scripts
execute_scripts() {
    local API_SCRIPT_NAME=$1  # Name of the Python script to execute

    cd "${PROJECT_PATH}/scripts/api_scripts"
    # Call the Python script
    $PYTHON_EXECUTABLE "$API_SCRIPT_NAME"

    # Process JSON files and insert them into the database
    process_json_files
}

# Execute scripts for different APIs and remove dead links
execute_scripts "wmAPI.py"      # For Walmart API
execute_scripts "tAPI.py"       # For Target API
execute_scripts "Parsehub.py"   # For Parsehub API

# Remove Dead Links
cd "${PROJECT_PATH}/scripts/database_scripts"
$NODE_EXECUTABLE "Remove_Dead_Links_DB.js"
