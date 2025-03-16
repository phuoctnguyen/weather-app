import requests
import sys

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        
        return weather
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(weather):
    if weather:
        print(f"\nWeather in {weather['city']}:\n")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Condition: {weather['description'].title()}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s\n")
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    API_KEY = "bce6f46add7b3ede49bee75169de8399"  # Replace with your API key
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name, API_KEY)
    display_weather(weather_data)
