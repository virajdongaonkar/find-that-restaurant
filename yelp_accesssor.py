import json

#from requests.auth import HTTPBasicAuth
#import requests

reader = open('credentials.txt', 'r')
credentials = reader.readlines()

url = 'https://api.yelp.com/v3'

auth = 'Bearer ' + credentials[1]
print(auth)
headers = {'Content-Type': 'application/json', 'Authorization': auth}

reader.close()