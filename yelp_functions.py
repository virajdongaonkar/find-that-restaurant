# This file contains the functions that interact with the Yelp API

import requests

# This function searches for businesses based on keywords.
def keyword_search(URL, headers):
    URL += 'businesses/search'
    term = input('Enter the keyword: ')
    location = input("Enter the location (\"city, state\" or \"zipcode\") of the restaurant: ")

    # defining parameters to be sent to the API
    PARAMS = {'term': term, 'location':location}
    
    # This GET request calls the keyword Yelp Fusion API.
    r = requests.get(url = URL, headers=headers, params = PARAMS)
    
    # extracting data
    data = r.json()

    print("Some possible businesses could be: ")

    # This code block numbers the possible businesses
    numbering = 0

    for business in data['businesses']:
        print(str(numbering) + " " + business['name'])
        numbering += 1

    chosen = input("Choose the number that you were looking for (\"-1\" if not found): ")
    
    try:
        chosen = int(chosen)
        if chosen is not -1:    # This is the case where the business was found.
            URL = 'https://api.yelp.com/v3/businesses/' + data['businesses'][chosen]['id']
            data = business_data(URL, headers)

            print_data(data)
        else:  
            print("Hope we can find the restaurant next time!")
    except:
        print("Invalid input")

# This function searches for businesses based on phone numbers.
def phone_search(URL, headers):
    URL += 'businesses/search/phone'
    
    phone_number = input('Searching for phone number: ')
    params = {'phone': phone_number}

    # This GET request calls the phone number Yelp Fusion API.
    re = requests.get(url = URL, headers=headers, params=params)
    data = re.json()

    URL = 'https://api.yelp.com/v3/businesses/' + data['businesses'][0]['id']
    data = business_data(URL, headers)
    print_data(data)

# This function returns the data of the selected business based off their Yelp ID.
def business_data(URL, headers):
    re = requests.get(url = URL, headers=headers)
    data = re.json()
    return data

# This function prints the data of the selected business.
def print_data(data):
    name = data['name']
    website = data['url'] 
    phone_number = data['display_phone']
    
    # Gathers all categories of the business
    categories = []
    for category in data['categories']:
        categories.append(category['title'])
    
    rating = data['rating']
    address = data['location']['display_address']

    print("Here is all the details for " + name)
    print('Yelp website: ',  website)
    print('Address: ',  address)
    print('Phone number:',  phone_number)
    print('Categories: ',  categories)
    print('Rating: ',  rating)