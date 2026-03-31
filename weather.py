import requests

def fetch_weather(api_key, location):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            
            print(f"Weather in {location}:")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temperature} °C")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"Error fetching weather data: {str(e)}")

if _name_ == "_main_":
    api_key = 'OpenWeatherMap'  # Replace with your OpenWeatherMap API key
    location = input("Enter city name or ZIP code: ")
    fetch_weather(api_key, location)
