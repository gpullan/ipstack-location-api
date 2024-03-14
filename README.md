# ipstack-location-api
This CLI command is designed to provide the longitude and latitude of any provided IP address.

The correct format is: python iplocation.py -i <IP_ADDRESS> -a <API_KEY>

If you do not already have an API-Key you will first need to register at www.ipstack.com

#### Security

Currently this application is designed to take the API-Key as one of the command line options...this may not be the best approach as the command line details would be available in the history of the console.  More secure approaches could be either to:

   ask for the api-key during the run on the command (this would mean that the command would be unable to be used in scripting and automation tools)
   Run the command as a part of a pipeline (This would enable the api-key to passed in securely i.e. github workflows and such like)
   incorporate a local secure method to pass credentials such as vault
