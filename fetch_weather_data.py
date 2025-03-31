import requests
import json

API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(url)
    return response.json()

def main():
    city = 'New York'
    weather_data = get_weather(city)
    print(json.dumps(weather_data, indent=4))

if __name__ == "__main__":
    main()
