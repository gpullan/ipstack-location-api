import requests
import argparse
import json
import re

def get_location(ip_address, api_key):
    # Make a GET request to the IPStack API
    response = requests.get(f"http://api.ipstack.com/{ip_address}?access_key={api_key}")

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        return latitude, longitude
    else:
        print("Error occurred while fetching location data.")
        return None

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="IP address")
    parser.add_argument("-a", "--api-key", help="API key")
    args = parser.parse_args()

    # Check if the IP address and API key are provided
    if not args.ip or not args.api_key:
        print("Please provide an IP address and API key.")
        print("The correct format is: python iplocation.py -i <IP_ADDRESS> -a <API_KEY>")
        return
    
    ip_address = args.ip
    # Check if the IP address is in the correct format
    if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip_address):
        print("Invalid IP address format.")
        return

    api_key = args.api_key
    # Check if the API key is in the correct format
    if not re.match(r"^[a-fA-F0-9]{32}$", api_key):
        print("Invalid API key format.")
        return

    latitude, longitude = get_location(ip_address, api_key)

    if latitude and longitude:
        location = {
            "latitude": latitude,
            "longitude": longitude
        }
        print(json.dumps(location))
    else:
        print("Error occurred while fetching location data.")

if __name__ == "__main__":
    main()
