import requests as req
    
def req_url():
    def sep():
        print('=' * 65)
        
    API_KEY = ''    
        
    # default URL
    link = 'http://api.weatherapi.com/v1'
    
    # requests logic
    cur_weath = '/current.json' # implement current weather data param
    forecast = '/forecast.json' # implement overall forecast
    
    r = req.get(link)
    
    # user init payload params
    zip_code = int(input('Enter your Zip Code:\n'))
    num_days = int(input('Enter number of Days: (1-7)\n'))
    # zip_code = '26301'
    # num_days = '2'
    
    payload = {'key': API_KEY, 'q': zip_code, 'days': num_days} # parameters
    
    # format URL
    request_url = f'{link}{cur_weath}'
    r = req.get(request_url, params=payload) 
    
    # call information
    info = r.json()
    
    # data table
    location_data = info['location']
    current_data = info['current']
    
    # format terminal
    sep()
    print('API URL:', r.url)
    # status code for error handling
    print("Status Code:", r.status_code)
    sep()
    
    # loop through key/value pairs
    for key, value in current_data.items():
        if key == 'condition':
            print(f"condition: {value['text']}")
        else:
            print(f"{key}: {value}")
    
    sep()
    # Location data loop     
    for key, value in location_data.items():
        if key == 'condition':
            print(f"condition: {value['text']}")
        else:
            print(f"{key}: {value}")

# display URL
req_url()