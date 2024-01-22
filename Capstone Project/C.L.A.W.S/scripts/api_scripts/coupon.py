import requests
import json

# API endpoint to get store and coupon data
api_url = "https://get-promo-codes.p.rapidapi.com/data/get-coupons/"

# Make a request to the API
response = requests.get(api_url, params={"page": "1", "sort": "update_time_desc"}, headers={"X-RapidAPI-Key": "b897423251msh77f56ef82b87fffp18425djsn6ccc2ba2e0bc"})

# Check for a successful API response
if response.status_code == 200:
    api_data = response.json()

    # Initialize a list to hold coupon data
    coupons = []

    # Iterate through API data
    for coupon_data in api_data["data"]:
        # Extract relevant data
        store_url = coupon_data["url"]
        coupon_code = coupon_data["code"]

        # Append coupon information to the list
        coupons.append({
            "store_url": store_url,
            "coupon_code": coupon_code
        })

    # Write the coupon data to a JSON file
    with open('/home/workspace/Software-Engineering-Project-Course/scripts/json_files/coupons.json', 'w') as file:
        json.dump(coupons, file, indent=4)

    print("Coupons data written to coupons.json")

else:
    print("API request with status code coupon:", response.status_code)
