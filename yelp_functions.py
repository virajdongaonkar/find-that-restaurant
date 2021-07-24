import requests

def keyword_search(URL, headers):
    print('Searching for keyword.')

    location = "78705"

    # defining parameters to be sent to the API
    PARAMS = {'location':location}
    
    # sending get request 
    r = requests.get(url = URL, headers=headers, params = PARAMS)
    
    # extracting data
    data = r.json()
    #print(data)

def phone_search(URL, headers):
    print('Searching for phone number.')