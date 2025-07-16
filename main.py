import requests as req

# API key
API_KEY = '00a142a6d6ae4444af353824251607'
    
def req_url():
    def sep():
        print('=' * 65)
        
    # default URL
    link = 'http://api.weatherapi.com/v1'
    
    # user choice
    choice = input("Get 'current' weather or a 'forecast'? ").lower().strip()
    # zip
    zip_code = input('Enter your Zip Code:\n')
    
    # datasets
    endpoint = ''
    payload = {}
    
    # set endpoint and payload based on choice
    if choice == 'current':
        endpoint = '/current.json'
        payload = {'key': API_KEY, 'q': zip_code}
        
    elif choice == 'forecast':
        endpoint = '/forecast.json'
        # Only ask for number of days if forecast is selected
        num_days = int(input('Enter number of Days (1-14):\n'))
        payload = {'key': API_KEY, 'q': zip_code, 'days': num_days}

    else:
        print("\nInvalid choice. Please enter 'current' or 'forecast'.")
    
    # format URL
    request_url = f'{link}{endpoint}'
    r = req.get(request_url, params=payload) 
    
    # call information
    info = r.json()
    location_data = info['location']
    
     # format terminal
    sep()
    if r.status_code != 200:
        sep()
        print(f"Error: Status Code {r.status_code}")
        print(f"API Response: {r.text}")
        sep()
    else:
        print("Status Code:", r.status_code)
    sep()
    print(f"\nLocation: {location_data['name']}, {location_data['region']} \n")
    
    if choice == 'current':
        current_data = info['current']
        
        # Loop through key/value pairs for current weather
        for key, value in current_data.items():
            if key == 'condition':
                print(f"condition: {value['text']}")
            else:
                print(f"{key}: {value}")
    
    elif choice == 'forecast':
        forecast_days = info['forecast']['forecastday']
        print(f"Found {len(forecast_days)}-day forecast:")
        
        for day_data in forecast_days:
            sep()
            print(f"Date: {day_data['date']}")
            day_info = day_data['day']
            print(f"  Max Temp:  {day_info['maxtemp_f']}F")
            print(f"  Min Temp:  {day_info['mintemp_f']}F")
            print(f"  Condition: {day_info['condition']['text']}")

# display URL
req_url()