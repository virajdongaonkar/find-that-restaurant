import json
import requests

reader = open('credentials.txt', 'r')
credentials = reader.readlines()
API_KEY = credentials[1]
headers = {
        'Authorization': 'Bearer %s' % API_KEY,
}
reader.close()
  
# api-endpoint
URL = "https://api.yelp.com/v3/businesses/search"

location = "78705"


# defining parameters to be sent to the API
PARAMS = {'location':location}
  
# sending get request 
r = requests.get(url = URL, headers=headers, params = PARAMS)
  
# extracting data
data = r.json()

print(data)
