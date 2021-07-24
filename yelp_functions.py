# This file contains the functions that interact with the Yelp API

import requests

# This function searches for businesses based on keywords.
def keyword_search(URL, headers):
    URL += 'businesses/search'
    term = input('Enter the keyword: ')
    location = input("Enter the location (\"city, state\" or \"zipcode\") of the restaurant: ")

    # defining parameters to be sent to the API
    PARAMS = {'term': term, 'location':location}
    
    # sending get request 
    r = requests.get(url = URL, headers=headers, params = PARAMS)
    
    # extracting data
    data = r.json()

    print("Some possible restaurants could be: ")

    numbering = 0

    for business in data['businesses']:
        print(str(numbering) + " " + business['name'])
        numbering += 1

    chosen = input("Choose the number that you were looking for (\"-1\" if not found): ")
    
    try:
        chosen = int(chosen)
        if chosen is not -1:
            name = data['businesses'][chosen]['name']
            print("Here is all the details for " + name)
            URL = 'https://api.yelp.com/v3/businesses/' + data['businesses'][chosen]['id']
            re = requests.get(url = URL, headers=headers)
            data = re.json()

            website = data['url'] 
            phone_number = data['display_phone']
            categories = []
            for category in data['categories']:
                categories.append(category['title'])
            rating = data['rating']
            address = data['location']['display_address']

            #start = []
            #end = []

            #for day in data['hours'][0]['open']:
            #    start.append(day['start'])
            #    end.append(day['end'])
 
            print('Yelp website: ',  website)
            print('Address: ',  address)
            print('Phone number:',  phone_number)
            print('Categories: ',  categories)
            print('Rating: ',  rating)
        else:
            print("Hope we can find the restaurant next time!")
    except:
        print("Invalid input")

# This function searches for businesses based on phone numbers.
def phone_search(URL, headers):
    print('Searching for phone number.')