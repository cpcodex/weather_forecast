import requests as req
import os
from dotenv import load_dotenv

# load .env
load_dotenv()

# API key
API_KEY = os.getenv("API_KEY")

# default URL
link = "http://api.weatherapi.com/v1"

def sep():
    print("=" * 65)

def user_input():
    # user choice
    choice = input("'current' weather or the 'forecast'?\n").lower().strip()

    if choice not in ['current', 'forecast']:
        print("\nInvalid choice. Please enter 'current' or 'forecast'.")
        return None, None, None

    # zip
    zip_code = input("Enter your Zip Code:\n")
    
    # set endpoint and payload based on choice
    if choice == "current":
        endpoint = "/current.json"
        payload = {"key": API_KEY, "q": zip_code}
    else:
        endpoint = "/forecast.json"
        # Only ask for number of days if forecast is selected
        num_days = int(input("Enter number of Days (1-14):\n"))
        payload = {"key": API_KEY, "q": zip_code, "days": num_days}
        
    return choice, endpoint, payload
    
def weather_data(endpoint, payload):
    # format URL
    request_url = f"{link}{endpoint}"
    r = req.get(request_url, params=payload)
    
    # call information
    info = r.json()
    return info
    

def display_current_weather(info):
    # index dataset
    current = info['current']
    
    print(f"Current Weather:")
    sep()
    # Directly access and print only the desired key-value pairs
    print(f"  Current Temp: {current['temp_f']}F")
    print(f"  Feels Like:   {current['feelslike_f']}F")
    print(f"  Condition:    {current['condition']['text']}")

def display_forecast(info):
    # index dataset
    forecast_days = info["forecast"]["forecastday"]
    
    print(f"\nFound {len(forecast_days)}-day forecast:\n")

    for day_data in forecast_days:
        sep()
        print(f"Date: {day_data['date']}")
        day_info = day_data["day"]
        print(f"  Max Temp:  {day_info['maxtemp_f']}F")
        print(f"  Min Temp:  {day_info['mintemp_f']}F")
        print(f"  Condition: {day_info['condition']['text']}")

def main():
    choice, endpoint, payload = user_input()
     # error handle
    if not choice:
        return
    
    sep()
    info = weather_data(endpoint, payload)
    # error handle
    if not info:
        return
    
    # location data
    location = info['location']
    print(f"\nLocation: {location['name']}, {location['region']}\n")
    
    sep()
    # format terminal
    if choice == "current":
        display_current_weather(info)
    else:
        display_forecast(info)
    sep()

if __name__ == "__main__":
    main()