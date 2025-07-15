"""
API key from weather service provider

utilize intall requests with pip

make API request calls, fetch weather data city or location

Parse the JSON data, extract necessary data

Display weather information in the terminal

Handle all errors
"""
# libraries
import requests as req

def sep():
    print('=' * 65)
    
def req_url():
    sep()
    print('API URL:', r.url)
    sep()

# requests logic
r = req.get('http://api.weatherapi.com/v1')
r_type = '/current.json' # implement current weather data param
payload = {'q': '26301', 'days': '2'} # parameters

# format URL
r = req.get(f'http://api.weatherapi.com/v1{r_type}', params=payload)
# display URL
req_url()