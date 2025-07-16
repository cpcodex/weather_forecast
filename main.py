import requests as req

# API key, TODO add .env for API key
API_KEY = ""


def sep():
    print("=" * 65)

# default URL
link = "http://api.weatherapi.com/v1"

# user choice
choice = input("Get 'current' weather or a 'forecast'?\n").lower().strip()
# zip
zip_code = input("Enter your Zip Code:\n")

# datasets
endpoint = ""
payload = {}

# set endpoint and payload based on choice
if choice == "current":
    endpoint = "/current.json"
    payload = {"key": API_KEY, "q": zip_code}

elif choice == "forecast":
    endpoint = "/forecast.json"
    # Only ask for number of days if forecast is selected
    num_days = int(input("Enter number of Days (1-14):\n"))
    payload = {"key": API_KEY, "q": zip_code, "days": num_days}

else:
    print("\nInvalid choice. Please enter 'current' or 'forecast'.")

# format URL
request_url = f"{link}{endpoint}"
r = req.get(request_url, params=payload)

# call information
info = r.json()
location_data = info["location"]

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

# process response based on choice
if choice == "current":
    location = info['location']
    current = info['current']

    print(f"Current Weather:")
    sep()
    # Directly access and print only the desired key-value pairs
    print(f"  Current Temp: {current['temp_f']}F")
    print(f"  Feels Like:   {current['feelslike_f']}F")
    print(f"  Condition:    {current['condition']['text']}")

elif choice == "forecast":
    forecast_days = info["forecast"]["forecastday"]
    print(f"Found {len(forecast_days)}-day forecast:")

    for day_data in forecast_days:
        sep()
        print(f"Date: {day_data['date']}")
        day_info = day_data["day"]
        print(f"  Max Temp:  {day_info['maxtemp_f']}F")
        print(f"  Min Temp:  {day_info['mintemp_f']}F")
        print(f"  Condition: {day_info['condition']['text']}")