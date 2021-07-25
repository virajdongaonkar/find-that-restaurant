import json

from yelp_functions import keyword_search, phone_search

# This block of code finds the API_KEY from the credentials.txt file and puts it in a header dict.
reader = open('credentials.txt', 'r')
credentials = reader.readlines()
API_KEY = credentials[1]    # Second line of credentials.txt should have API key
headers = {
        'Authorization': 'Bearer %s' % API_KEY,
}
reader.close()
  
# This is the URL of the api-endpoint
URL = "https://api.yelp.com/v3/"

# This block of code keeps track of user response and acts accordingly.
response = -1

while response < 1 or response > 2:
        response = input("Press 1 to search for a business by keyword, category, location, or price level.\nPress 2 to search for business by telephone number.\n")

        try:
                response = int(response)
                if response is 1:       # This path follows a search based off keyword.
                        keyword_search(URL, headers)
                elif response is 2:     # This path follows a search based off phone number.
                        phone_search(URL, headers)
                else:
                        print("Invalid response, try again.")
        except:
                print("Invalid response.")

