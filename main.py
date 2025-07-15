import requests as req
    
def req_url():
    def sep():
        print('=' * 65)
        
    sep()
    print('API URL:', r.url)
    sep()

# default URL
link = 'http://api.weatherapi.com/v1'
r = req.get(link)

# requests logic
cur_weath = '/current.json' # implement current weather data param
forecast = '/forecast.json' # implement overall forecast

# user init payload params
# zip_code = int(input('Enter your Zip Code:\n'))
# num_days = int(input('Enter number of Days: (1-7)\n'))
zip_code = '26301'
num_days = '2'
payload = {'q': zip_code, 'days': num_days} # parameters

# format URL
r = req.get(f'{link}{cur_weath}', params=payload)
# display URL
req_url()

print("Status Code:", r.status_code)