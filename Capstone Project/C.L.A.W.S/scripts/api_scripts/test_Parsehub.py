#IMPORTS
import pytest
import tempfile
import os
from unittest.mock import Mock, patch

#FIXTURES AND MOCKS

#Get configs
@pytest.fixture
def config_data():
    env_values = dotenv_values("ph.env")
    env_values = dict(env_values)                               #Read env_values into a dictionary of the same name
    projects = json.loads(env_values["projects"])               #A list of tuples each containing:
                                                                    #A project token to a project that scrapes a particular store
                                                                    #The related store's name
                                                                    #The string used in that store's URLs to represent a space in a search
                                                                    #A URL template that when contatenated with a search "term" will pull up a search results page
    ph_config = {                                               #The configurations needed to run any parsehub project
        "api_key":env_values["api_key"],                        #The developer's API key
        "start_url":env_values["start_url"]                     #The URL to start the scraping from, Default: None
    }
    em_config = {                                               #The configurations needed to send an error email to the developer
        "sender_email":env_values["sender_email"],              #The email address of the message sender
        "app_password":env_values["app_password"],              #The password to the email address of the message sender
        "receiver_email":env_values["receiver_email"]           #The email address of the message receiver
    }

    return ph_config, em_config, projects                       #Return the Parsehub configurations, email configurations, and project tuples 
    
#ENV_PARSER TESTS
#Open and return the env file to be parsed and tested
@pytest.fixture
def env_data():                                         
    env_values = dotenv_values("ph.env")
    return env_values
    

#Test that the function is returning three variables and that each variable is the correct size 
def test_env_parser():
    #Run the env_parser to be tested
    results = env_parser(env_data)

    #Check that all env variables and fields within are present
    assert r_size == 3, "env_parser() returned {r_size} results, expected 3."      

    #Check the size of the parsehub configurations
    ph_config = results[0]
    ph_size = ph_config.size()
    assert ph_size == 2, "env_parser() returned {ph_size} fields in the Parsehub Config, expected 2."

    #Check the size of the email configurations
    em_config = results[1]
    em_size = em_config.size()
    assert em_size == 3, "env_parser() returned {em_size} fields in the Email Config, expected 3."

    #Check that each tuple in projects is a size of 4
    projects = results[2]
    count = 0
    for tuple in projects:
        tpl_size = tuple.size()
        assert tpl_size == 4, "Tuple {count} in projects has {tpl_size} fields, expected 4."
        count += 1

#URL_CREATOR TESTS
#Create the variables needed to run the function
@pytest.fixture
def url_creator_data():
    #Create a temporary file to hold search terms both with and without trailing spaces
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Refrigerator")                                                 #Single word without trailing spaces
        temp_file.write("Coffee Maker")                                                 #Two words without trailing spaces
        temp_file.write("Television ")                                                  #Single word with trailing spaces
        temp_file.write("Oven Timer ")                                                  #Two words with trailing spaces
    temp_file_name = temp_file.name                                                     #Get file name
    
    #project tuples, project key and store name unnecessary for test, includes different space and url template strings
    project = [["_", "_", "%20", "https://www.website.com/site/searchpage.st="],        
              ["_", "_", "+", "https://www.store.com/site/searchpage.st="]]
    
    return temp_file_name, projects


#Test that url_creator() is returning the correct number of urls, and that it is replacing spaces in the search terms with the correct space string.
def test_url_creator():
    with patch('Parsehub.is_valid_url') as mock_is_valid_url, patch('Parsehub.send_error') as mock_send_error:
        mock_is_valid_url.return_value = True
        mock_send_error.return_value = None

        em_config = []
        url_list = []
        temp_file, projects = url_creator_data
        for proj in projects:
            urls = url_creator(em_config, temp_file, proj)
            url_list.append(urls)
        
        assert url_list.size() == 7, "url_creator() returned {url_list.size()} urls, expected 4."
        
        assert url_list[0] == "https://www.website.com/site/searchpage.st=Refrigerator", "url_creator() returned {url_list[0]}, expected https://www.website.com/site/searchpage.st=Refrigerator"
        assert url_list[1] == "https://www.website.com/site/searchpage.st=Coffee%20Maker", "url_creator() returned {url_list[1]}, expected https://www.website.com/site/searchp0age.st=Coffee%20Maker"
        assert url_list[2] == "https://www.website.com/site/searchpage.st=Television", "url_creator() returned {url_list[2]}, expected https://www.website.com/site/searchpage.st=Television"
        assert url_list[3] == "https://www.website.com/site/searchpage.st=Oven%20Timer", "url_creator() returned {url_list[3]}, https://www.website.com/site/searchpage.st=Oven%20Timer"
        assert url_list[4] == "https://www.store.com/site/searchpage.st=Refrigerator", "url_creator() returned {url_list[4]}, expected https://www.store.com/site/searchpage.st=Refrigerator"
        assert url_list[5] == "https://www.store.com/site/searchpage.st=Coffee+Maker", "url_creator() returned {url_list[5]}, expected https://www.store.com/site/searchpage.st=Coffee+Maker"
        assert url_list[6] == "https://www.store.com/site/searchpage.st=Television", "url_creator() returned {url_list[6]}, expected https://www.store.com/site/searchpage.st=Television"
        assert url_list[7] == "https://www.store.com/site/searchpage.st=Oven+Timer", "url_creator() returned {url_list[7]}, expected https://www.store.com/site/searchpage.st=Oven+Timer"
        
        os.remove(temp_file.name)

#IS_VALID_URL TESTS
#Test if is_valid_url() correctly identifies urls to pages that do and do not exist
def test_is_valid_url():
    valid_url = "https://www.google.com/"                                     #url to page that exists
    invalid_url = "https://www.website.com/invalid-url"                       #url to page that does not exist

    #Run test on the valid url, return True
    result = is_valid_url(valid_url)                                         
    assert result == True, "is_valid_url() returned {result} for a valid url, expected True."

    #Run test on the invalid url, return False
    result = is_valid_url(invalid_url)
    assert result == False, "is_valid_url() returned {result} for a invalid url, expected False."

#SEND_ERROR TESTS
#Test that send_error() calls all of the functions needed to send an email.
#Cannot test that error message was received without human intervention.
def test_send_error():
    with patch('smtplib.SMTP') as mock_smtp_class:
        # Configure the mock SMTP class
        mock_smtp_instance = mock_smtp_class.return_value

        #Get the email config data
        _, em_config, _ = config_data()

        #Call the send_error() with a code, message, and config data
        send_error(1, "https://www.website.com/invalid-url", em_config)

        #Test that each function was called the correct amount of times (once each)
        assert mock_smtp_class.call_count == 1, "SMTP class was not instantiated as expected."
        assert mock_smtp_instance.starttls.call_count == 1, "starttls() was not called as expected."
        assert mock_smtp_instance.login.call_count == 1, "login() was not called as expected."
        assert mock_smtp_instance.sendmail.call_count == 1, "sendmail() was not called as expected."
        assert mock_smtp_instance.quit.call_count == 1, "quit() was not called as expected."

#CHECK_VALUES TESTS
@pytest.fixture
def check_values_data():
    no_name = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                 "UPC": "placeholder_value",
                 "Price": "$39.00",
                 "Category_ID": "placeholder_value",
                 "Sub_Category_ID": "placeholder_value",
                 "Description": "Apple - MagSafe iPhone Charger - White",
                 "Keywords": [],
                 "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                 }]
    no_description = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                 "UPC": "placeholder_value",
                 "Name": "Apple - MagSafe iPhone Charger - White",
                 "Price": "$39.00",
                 "Category_ID": "placeholder_value",
                 "Sub_Category_ID": "placeholder_value",
                 "Keywords": [],
                 "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                 }]
    no_name_desc = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                 "UPC": "placeholder_value",
                 "Price": "$39.00",
                 "Category_ID": "placeholder_value",
                 "Sub_Category_ID": "placeholder_value",
                 "Keywords": [],
                 "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                 }]
    no_price = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                 "UPC": "placeholder_value",
                 "Name": "Apple - MagSafe iPhone Charger - White",
                 "Category_ID": "placeholder_value",
                 "Sub_Category_ID": "placeholder_value",
                 "Description": "Apple - MagSafe iPhone Charger - White",
                 "Keywords": [],
                 "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                 }]
    blank_price = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                    "UPC": "placeholder_value",
                    "Name": "Apple - MagSafe iPhone Charger - White",
                    "Price": "Check store for price",
                    "Category_ID": "placeholder_value",
                    "Sub_Category_ID": "placeholder_value",
                    "Description": "Apple - MagSafe iPhone Charger - White",
                    "Keywords": [],
                    "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                  }]
    no_img = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                 "UPC": "placeholder_value",
                 "Name": "Apple - MagSafe iPhone Charger - White",
                 "Price": "$39.00",
                 "Category_ID": "placeholder_value",
                 "Sub_Category_ID": "placeholder_value",
                 "Description": "Apple - MagSafe iPhone Charger - White",
                 "Keywords": [],
                 }]
    blank_img = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                 "UPC": "placeholder_value",
                 "Name": "Apple - MagSafe iPhone Charger - White",
                 "Price": "$39.00",
                 "Category_ID": "placeholder_value",
                 "Sub_Category_ID": "placeholder_value",
                 "Description": "Apple - MagSafe iPhone Charger - White",
                 "Keywords": [],
                 "Img_URL": "No Image"
                 }]
    return no_name, no_description, no_name_desc, no_price, blank_price, no_img, blank_img

def test_check_values():
    with patch('Parsehub.send_error') as mock_send_error:
        #Mock send_error()
        mock_send_error.return_value = None

        #Get the lists of dictionaries data
        no_name, no_description, no_name_desc, no_price, blank_price, no_img, blank_img = check_values_data

        #Check that the Name field was filled
        result = check_values(no_name)
        assert "Name" in result[0], "check_values() returned a dictionary with no Name field."
        
        #Check that the Description field was filled
        result = check_values(no_description)
        assert "Description" in result[0], "check_values() returned a dictionary with no Description field."

        #Check that the mock_send_error was called because neither Name or Description was properly scraped
        result = check_values(no_name_desc)
        assert mock_send_error.call_count == 1, "check_values() did not send an email when Name and Description were empty."

        #Check that the Price field exists
        result = check_values(no_price)
        assert "Price" in result[0], "check_values() returned a dictionary with no Price field."

        #Check that the mock_send_error was called because Price was not properly scraped
        result = check_values(blank_price)
        assert mock_send_error.call_count == 1, "check_values() did not send an email when Price was empty."

        #Check that the Img_URL field exists
        result = check_values(no_img)
        assert "Img_URL" in result[0], "check_values() returned a dictionary with no Img_URL field."

        #Check that the mock_send_error was called because Img_URL was not properly scraped
        result = check_values(blank_img)
        assert mock_send_error.call_count == 1, "check_values() did not send an email when Img_URL was empty."

#FORMATTER TESTS
#dictionaries
@pytest.fixture
def formatter_data():
    in_order = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                 "UPC": "placeholder_value",
                 "Name": "Apple - MagSafe iPhone Charger - White",
                 "Price": "$39.00",
                 "Category_ID": "placeholder_value",
                 "Sub_Category_ID": "placeholder_value",
                 "Description": "Apple - MagSafe iPhone Charger - White",
                 "Keywords": [],
                 "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                 }]
    out_of_order = [{"Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300",
                     "Name": "Apple - MagSafe iPhone Charger - White",
                     "Sub_Category_ID": "placeholder_value",
                     "URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                     "UPC": "placeholder_value",
                     "Keywords": [],
                     "Description": "Apple - MagSafe iPhone Charger - White",
                     "Price": "$39.00",
                     "Category_ID": "placeholder_value",
                     }]
    missing_fields = [{"UPC": "placeholder_value",
                       "Name": "Apple - MagSafe iPhone Charger - White",
                       "Category_ID": "placeholder_value",
                       "Sub_Category_ID": "placeholder_value",
                       "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                      }]
    miss_out_of_order = [{"Name": "Apple - MagSafe iPhone Charger - White",
                       "Category_ID": "placeholder_value",
                       "UPC": "placeholder_value",
                       "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300",
                       "Sub_Category_ID": "placeholder_value"
                      }]
    filled_fields = [{"URL": None,
                      "UPC": "placeholder_value",
                      "Name": "Apple - MagSafe iPhone Charger - White",
                      "Price": None,
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": None,
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                      }]
    return in_order, out_of_order, missing_fields, miss_out_of_order, filled_fields

def test_formatter():
    in_order, out_of_order, missing_fields, miss_out_of_order, filled_fields = formatter_data

    #Check that formatter returns an ordered dictionary when given an ordered dictionary
    result = formatter(in_order)
    assert result == in_order, "formatter() returned {result},\n expected {in_order}."

    #Check that formatter returns an ordered dictionary when given a unordered dictionary
    result = formatter(out_of_order)
    assert result == in_order, "formatter() returned {result},\n expected {in_order}."

    #Check that formatter returns an ordered dictionary with missing fields filled in when given a dictionary with missing fields
    result = formatter(missing_fields)
    assert result == filled_fields, "formatter() returned {result},\n expected {filled_fields}."

    #Check that formatter returns an ordered dictionary with missing fields filled in when given an unordered dictionary with missing fields
    result = formatter(miss_out_of_order)
    assert result == filled_fields, "formatter() returned {result},\n expected {filled_fields}."

#RM_DUPLICATE TESTS
#dictionaries
def rm_duplicate_data():
    no_duplicates = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                      "UPC": "placeholder_value",
                      "Name": "Apple - MagSafe iPhone Charger - White",
                      "Price": "$39.00",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "Apple - MagSafe iPhone Charger - White",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                     },
                     {"URL": "https://www.bestbuy.com/site/uag-monarch-pro-series-case-with-magsafe-for-apple-iphone-15-pro-carbon-fiber/6548413.p?skuId=6548413",
                      "UPC": "placeholder_value",
                      "Name": "UAG - Monarch Pro Series Case with Magsafe for Apple iPhone 15 Pro - Carbon Fiber",
                      "Price": "$79.95",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "UAG - Monarch Pro Series Case with Magsafe for Apple iPhone 15 Pro - Carbon Fiber",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6548/6548413_sd.jpg;maxHeight=200;maxWidth=300"  
                     },
                     {"URL": "https://www.bestbuy.com/site/smart-choice-5-8-safety-plus-stainless-steel-gas-range-connector/6684698.p?skuId=6684698",
                      "UPC": "placeholder_value",
                      "Name": "Smart Choice - 5/8'' Safety+PLUS Stainless-Steel Gas Range Connector",
                      "Price": "$39.99",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "Smart Choice - 5/8'' Safety+PLUS Stainless-Steel Gas Range Connector",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6684/6684698_sd.jpg;maxHeight=200;maxWidth=300"
                     }]
    all_duplicates = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                      "UPC": "placeholder_value",
                      "Name": "Apple - MagSafe iPhone Charger - White",
                      "Price": "$39.00",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "Apple - MagSafe iPhone Charger - White",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                     },
                     {"URL": "https://www.bestbuy.com/site/uag-monarch-pro-series-case-with-magsafe-for-apple-iphone-15-pro-carbon-fiber/6548413.p?skuId=6548413",
                      "UPC": "placeholder_value",
                      "Name": "UAG - Monarch Pro Series Case with Magsafe for Apple iPhone 15 Pro - Carbon Fiber",
                      "Price": "$79.95",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "UAG - Monarch Pro Series Case with Magsafe for Apple iPhone 15 Pro - Carbon Fiber",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6548/6548413_sd.jpg;maxHeight=200;maxWidth=300"  
                     },
                     {"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                      "UPC": "placeholder_value",
                      "Name": "Apple - MagSafe iPhone Charger - White",
                      "Price": "$39.00",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "Apple - MagSafe iPhone Charger - White",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                     },
                     {"URL": "https://www.bestbuy.com/site/smart-choice-5-8-safety-plus-stainless-steel-gas-range-connector/6684698.p?skuId=6684698",
                      "UPC": "placeholder_value",
                      "Name": "Smart Choice - 5/8'' Safety+PLUS Stainless-Steel Gas Range Connector",
                      "Price": "$39.99",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "Smart Choice - 5/8'' Safety+PLUS Stainless-Steel Gas Range Connector",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6684/6684698_sd.jpg;maxHeight=200;maxWidth=300"
                     },
                     {"URL": "https://www.bestbuy.com/site/uag-monarch-pro-series-case-with-magsafe-for-apple-iphone-15-pro-carbon-fiber/6548413.p?skuId=6548413",
                      "UPC": "placeholder_value",
                      "Name": "UAG - Monarch Pro Series Case with Magsafe for Apple iPhone 15 Pro - Carbon Fiber",
                      "Price": "$79.95",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "UAG - Monarch Pro Series Case with Magsafe for Apple iPhone 15 Pro - Carbon Fiber",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6548/6548413_sd.jpg;maxHeight=200;maxWidth=300"  
                     },
                     {"URL": "https://www.bestbuy.com/site/smart-choice-5-8-safety-plus-stainless-steel-gas-range-connector/6684698.p?skuId=6684698",
                      "UPC": "placeholder_value",
                      "Name": "Smart Choice - 5/8'' Safety+PLUS Stainless-Steel Gas Range Connector",
                      "Price": "$39.99",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "Smart Choice - 5/8'' Safety+PLUS Stainless-Steel Gas Range Connector",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6684/6684698_sd.jpg;maxHeight=200;maxWidth=300"
                     }]
    some_duplicates = [{"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                      "UPC": "placeholder_value",
                      "Name": "Apple - MagSafe iPhone Charger - White",
                      "Price": "$39.00",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "Apple - MagSafe iPhone Charger - White",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                     },
                     {"URL": "https://www.bestbuy.com/site/apple-magsafe-iphone-charger-white/6341029.p?skuId=6341029",
                      "UPC": "placeholder_value",
                      "Name": "Apple - MagSafe iPhone Charger - White",
                      "Price": "$39.00",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "Apple - MagSafe iPhone Charger - White",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6341/6341029_sd.jpg;maxHeight=200;maxWidth=300"
                     },
                     {"URL": "https://www.bestbuy.com/site/uag-monarch-pro-series-case-with-magsafe-for-apple-iphone-15-pro-carbon-fiber/6548413.p?skuId=6548413",
                      "UPC": "placeholder_value",
                      "Name": "UAG - Monarch Pro Series Case with Magsafe for Apple iPhone 15 Pro - Carbon Fiber",
                      "Price": "$79.95",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "UAG - Monarch Pro Series Case with Magsafe for Apple iPhone 15 Pro - Carbon Fiber",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6548/6548413_sd.jpg;maxHeight=200;maxWidth=300"  
                     },
                     {"URL": "https://www.bestbuy.com/site/smart-choice-5-8-safety-plus-stainless-steel-gas-range-connector/6684698.p?skuId=6684698",
                      "UPC": "placeholder_value",
                      "Name": "Smart Choice - 5/8'' Safety+PLUS Stainless-Steel Gas Range Connector",
                      "Price": "$39.99",
                      "Category_ID": "placeholder_value",
                      "Sub_Category_ID": "placeholder_value",
                      "Description": "Smart Choice - 5/8'' Safety+PLUS Stainless-Steel Gas Range Connector",
                      "Keywords": [],
                      "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6684/6684698_sd.jpg;maxHeight=200;maxWidth=300"
                     },
                     {"URL": "https://www.bestbuy.com/site/uag-monarch-pro-series-case-with-magsafe-for-apple-iphone-15-pro-carbon-fiber/6548413.p?skuId=6548413",
                     "UPC": "placeholder_value",
                     "Name": "UAG - Monarch Pro Series Case with Magsafe for Apple iPhone 15 Pro - Carbon Fiber",
                     "Price": "$79.95",
                     "Category_ID": "placeholder_value",
                     "Sub_Category_ID": "placeholder_value",
                     "Description": "UAG - Monarch Pro Series Case with Magsafe for Apple iPhone 15 Pro - Carbon Fiber",
                     "Keywords": [],
                     "Img_URL": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6548/6548413_sd.jpg;maxHeight=200;maxWidth=300"  
                     }]
    return no_duplicates, all_duplicates, some_duplicates
                        

def test_rm_duplicate():
    #Get the lists of dictionaries data
    no_duplicates, all_duplicates, some_duplicates = rm_duplicate_data

    #Check that rm_duplicate returns a list with no duplicate dictionaries when given a list with no duplicate dictionaries
    result = rm_duplicate(no_duplicates)
    assert result == no_duplicates, "no_duplicate() returned {result},\n expected {no_duplicates}."

    #Check that rm_duplicate returns a list with no duplicate dictionaries when given a list where every dictionary has a duplicate
    result = rm_duplicate(all_duplicates)
    assert result == 3, "no_duplicate() returned {result},\n expected {no_duplicates}."

    #Check that rm_duplicate returns a list with no duplicate dictionaries when given a list with some duplicate dictionaries
    result = rm_duplicate(some_duplicates)
    assert result == 3, "no_duplicate() returned {result},\n expected {no_duplicates}."

####################################################################################################################################################
    
#RUN_PROJECT TESTS

#Can't be tested because websites and urls change?
    
#Run with no products
#Run for wrong store
#Run with a few product results at correct store
#Run for invalid url
#Run for correct store but not a results page