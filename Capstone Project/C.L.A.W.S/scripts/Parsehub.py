#DEFINITION
#Program inteded to automate the use of the Parsehub project that pulls product data from various categories and subcategories. This program reads in two input json files,
#one that contains a list of all the categories and their respective urls for the products to be scrapped, and the other contains the parameter data for the project and run
#calls to succeed. A project is run for a single url at a time, as the run is pulling the data a while loop checks the completion status of the run every 60 seconds. Once all
#the data has been successfully pulled the data is converted into a json file and saved in the output folder, if the json represents a category and not a subcategory. If the
#json is a subcategory, all subcategories are collated into a single json file and then saved to the output folder.

#IMPORTS
import requests
import json
import sys
import time
import os

#RUN_PROJECT DEFINITION
def run_project(url, params):
    """
    Runs a Parsehub project on the given URL and retrieves data.
    
    Args:
        url (str): The URL to start the project.
        params (dict): A dictionary of parameters for the project.

    Returns:
        dict: The collected data as a dictionary.
    """
    
    #Add the url as 'start_url' to the params dictionary
    params['start_url'] = url
    #Start running a premade project using the api and starting_url provided, recieve data on the new run
    r = requests.post("https://www.parsehub.com/api/v2/projects/tgRrzKkvrR7f/run", data=params)
    #Parse recent run data into a dictionary
    rjson = r.json()
    #Get the new run_token from the dictionary
    run_token = rjson['run_token']
    while True:
        run = requests.get(f'https://www.parsehub.com/api/v2/runs/{run_token}', params=params)
        run_json = run.json()
        run_status = run_json['status']
        print(run_status)
        if (run_status == 'complete' or run_status == 'error'):
            if (run_status == 'error'):
                print("Error running project, quitting program")
                time.sleep(20)
                sys.exit(1)
            break
        time.sleep(60)  # Wait for 60 seconds before checking again
    data_json =requests.get(f'https://www.parsehub.com/api/v2/runs/{run_token}/data', params=params)
    data_dict = data_json.json()
    return data_dict

#MAIN FUNCTION
def main():
    #VARIABLE DECLARATIONS
    params_path = "../data/input/params.json"           #Path to the parameters json input file
    urls_path = "../data/input/Cat_URLs.json"           #Path to the category urls json input file
    json_path = "../data/output/BestBuy.json"           #Path to place the final json output file
    final_json = {}                                     #Dictionary to collate all data
    
    #Read in the parameters from the params.json into a params varaiable
    with open(params_path, "r") as json_file:
        params = json.load(json_file)
    #Read in the Category/Subcategory urls from the Cat_URLs.json
    with open(urls_path, "r") as json_file:
        urls = json.load(json_file)
    #Iterate through the urls running the project on them and saving the json files.
    #For each Category in the url list
    for category in urls["Categories"]:
        #If subcategories exist in the category
        if "Subcategory" in category:
            #Get the list of subcategories in category
            subcategories = category["Subcategory"]
            #For each subcategory get the subcategory name(throw away) and url
            for sub_name, sub_url in subcategories.items():
                #Call run_project on the subcategory url, recieve a dictionary of the data collected
                sub_dict = run_project(sub_url, params)
                #Add the collected data to the final_json
                final_json.update(sub_dict)
        #If there are no subcategories
        else:
            #Get the category url
            cat_url = category["URL"]
            #Call run_project on the category url, recieve a dictionary of the data collected
            cat_dict = run_project(cat_url, params)
            #Add the collected data to the final_json
            final_json.update(cat_dict)
    #Write the final_json dictionary as a json file in the output folder
    with open(json_path, 'w') as json_file:
        json.dump(final_json, json_file)