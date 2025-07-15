import requests as req
    
def req_url():
    def sep():
        print('=' * 65)
        
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