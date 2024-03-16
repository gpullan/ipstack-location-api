import requests
import argparse
import json
import re
import sys

def get_location(ip_address, api_key):
    """
    Retrieves the latitude and longitude of a given IP address using the IPStack API.

    Args:
        ip_address (str): The IP address to retrieve the location for.
        api_key (str): The API key for accessing the IPStack API.

    Returns:
        tuple: A tuple containing the latitude and longitude of the IP address.
               Returns None if an error occurred while fetching the location data.
    """
    # Make a GET request to the IPStack API
    try:
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
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {str(e)}")
        return None

def main():
    """
    Parses command line arguments and retrieves the location for a given IP address.

    The IP address and API key are provided as command line arguments.
    The correct format for running the script is: python iplocation.py -i <IP_ADDRESS> -a <API_KEY>
    """
    # Create an argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="IP address")
    parser.add_argument("-a", "--api-key", help="API key")
    args = parser.parse_args()

    # Check if the IP address and API key are provided
    if not args.ip or not args.api_key:
        print("Please provide an IP address and API key.")
        print("The correct format is: python iplocation.py -i <IP_ADDRESS> -a <API_KEY>")
        sys.exit(1)
    
    ip_address = args.ip
    # Check if the IP address is in the correct format
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_address):
        print("Invalid IP address format.")
        sys.exit(1)

    api_key = args.api_key
    # Check if the API key is in the correct format
    if not re.match(r"^[a-fA-F0-9]{32}$", api_key):
        print("Invalid API key format.")
        sys.exit(1)

    latitude, longitude = get_location(ip_address, api_key)

    if latitude and longitude:
        location = {
            "latitude": latitude,
            "longitude": longitude
        }
        print(json.dumps(location))
        sys.exit(0)
    else:
        print("Error occurred while fetching location data.")
        sys.exit(1)

if __name__ == "__main__":
    main()
