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

def parsehubpull():
    params = {
        "api_key": "tTz_xpHX9xtK",
        "start_url": "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&browsedCategory=pcmcat367400050001&id=pcat17071&iht=n&ks=960&list=y&qp=storepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~1387%5Estorepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~2516%5Estorepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~204%5Estorepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~1083%5Estorepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~181%5Estorepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~1153%5Estorepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~1082%5Estorepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~203%5Estorepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~828&sc=Global&st=categoryid%24pcmcat367400050001&type=page&usc=All%20Categories"
    }
    
    #Start running a premade project using the api and starting_url provided, recieve data on the new run
    r = requests.post("https://www.parsehub.com/api/v2/projects/tgRrzKkvrR7f/run", data=params)
    #Parse recent run data into a dictionary
    rjson = r.json()
    #Get the new run_token from the dictionary
    run_token = rjson['run_token']
    #While loop to check for when run finished successfully or with an error
    while True:
        #Get most recent data on most recent run
        run = requests.get(f'https://www.parsehub.com/api/v2/runs/{run_token}', params=params)
        #Parse run data into a dictionary
        run_json = run.json()
        #Get the status of the current run
        run_status = run_json['status']
        #If the run finished with a 'complete' or 'error' status
        if (run_status == 'complete' or run_status == 'error'):
            #If an 'error' status, print an error message and exit the program
            if (run_status == 'error'):
                print("Error running project, quitting program")
                time.sleep(20)
                sys.exit(1)
            #Else exit the loop
            break
        #If the run is not finished wait for 60 seconds before checking again
        time.sleep(60)
    #Pull the data collected by the most recent run
    data = requests.get(f'https://www.parsehub.com/api/v2/runs/{run_token}/data', params=params)
    #Parse the data from the run
    data_json = data.json()
    #Set a file_name for the json file
    file_name = "Bestbuy_Refridgerator.json"
    #Set the path to the output folder
    #directory_path = "../data/output/"
    #Get the full path
    #full_path = directory_path + file_name
    
    #With the file name provided write as a json file the parsed data to the current directory
    with open(file_name, 'w') as json_file:
        json.dump(data_json, json_file)