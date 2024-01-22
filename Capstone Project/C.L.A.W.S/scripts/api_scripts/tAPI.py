import requests
import json

# Function to read API key from file
def read_api_key(file_path):
    full_path = '/home/workspace/Software-Engineering-Project-Course/scripts/api_scripts/' + file_path
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "RedCircle" in line:
                parts = line.split('" = "')
                if len(parts) == 2:
                    return parts[1].replace('"', '').strip()
    return None

# Function to make API request
def make_api_request(api_key, search_term):
    params = {
        'api_key': api_key,
        'search_term': search_term,
        'type': 'search',
        'output': 'json'
    }
    response = requests.get('https://api.bluecartapi.com/request', params=params)
    return response.json()

# Read API key from file
api_key = read_api_key('api.env')
if api_key is None:
    print("API key not found")
    exit()

# List of search terms
search_terms = [
    'Bedding', 'Linens', 'Room Decorations', 'Kitchen and Dining', 'Storage',
    'Desk Supplies', 'Office Supplies', 'Laptops', 'Electronics', 'Gaming',
    'Smart Home', 'cables', 'mini fridge', 'microwave', 'cookware', 'appliances',
    'coffee makers', 'tea makers', 'cleaning supplies', 'laundry', 'clothing',
    'heating and cooling'
] # Add your search terms here

# Mapping of search terms to category and subcategory IDs
subcategory_mapping = {
    'Bedding': 1, 'Linens': 1, 'Room Decorations': 3, 'Kitchen and Dining': 5,
    'Storage': 4, 'Desk Supplies': 2, 'Office Supplies': 2, 'Laptops': 6,
    'Electronics': 2, 'Gaming': 8, 'Smart Home': 9, 'cables': 10, 
    'mini fridge': 11, 'microwave': 12, 'cookware': 5, 'appliances': 3,
    'coffee makers': 13, 'tea makers': 13, 'cleaning supplies': 14, 
    'laundry': 14, 'clothing': 1, 'heating and cooling': 15
}

category_mapping = {
    'Bedding': 1, 'Linens': 1, 'Room Decorations': 1, 'Kitchen and Dining': 1,
    'Storage': 1, 'Desk Supplies': 1, 'Office Supplies': 1, 'Laptops': 2,
    'Electronics': 2, 'Gaming': 2, 'Smart Home': 2, 'cables': 2, 
    'mini fridge': 3, 'microwave': 3, 'cookware': 3, 'appliances': 3,
    'coffee makers': 3, 'tea makers': 3, 'cleaning supplies': 3, 
    'laundry': 3, 'clothing': 1, 'heating and cooling': 3
}
storeName = 'TARGET'
# Loop through search terms and make requests
for term in search_terms:
    data = make_api_request(api_key, term)
    category_id = category_mapping.get(term, 0)
    subcategory_id = subcategory_mapping.get(term, 0)
    
    # Process the response and write to file
    template = {
        'Store': {
            'Name': storeName,
            'Products': []
        }
    }

    for result in data.get('search_results', []):
        product = result.get('product', {})
        offer = result.get('offers', {}).get('primary', {})
        template['Store']['Products'].append({
            'UPC': product.get('item_id', ''),
            'Name': product.get('title', ''),
            'Price': offer.get('price', ''),
            'Description': product.get('title', ''),
            'Img_URL': product.get('main_image', ''),
            'URL' : product.get('link',''),
            'Category_ID': category_id,
            'Sub_category_ID': subcategory_id
        })

    # Write result to a JSON file
    with open(f'/home/workspace/Software-Engineering-Project-Course/scripts/json_files/{term}.json', 'w') as file:
        json.dump(template, file, indent=2)
        print(f"File written for search term: {term}")
