from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Ensure API Key is loaded correctly
if not API_KEY:
    raise ValueError("API Key not found! Make sure you have a .env file with OPENWEATHER_API_KEY set.")

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"  # Fahrenheit
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
        print(f"Temperature: {weather['temperature']}°F")  # Fixed °F instead of °C
        print(f"Condition: {weather['description'].title()}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s\n")
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name, API_KEY)
    display_weather(weather_data)
