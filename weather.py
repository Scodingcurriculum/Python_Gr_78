import requests
API_KEY = 'fbe7f8ad10c2d09f1e348125c9daa6e4'  # Replace with your actual API key
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'latitude': weather_data['coord']['lat'],  #Additional:  Extracts latitude
            'longitude': weather_data['coord']['lon']  #Additional:  Extracts longitude
        }
    except requests.exceptions.RequestException as e:
        print("Error", f"Failed to get weather data: {e}")
        return None

def display_weather():
        city = input("Enter the name of the city: ")
        if city:
            weather = get_weather(city)
            if weather:
              print(f"City: {weather['city']}\n" 
                    f"Temperature: {weather['temperature']}°C\n"
                    f"Description: {weather['description']}\n"
                    f"Humidity: {weather['humidity']}%\n"
                     f"Latitude: {weather['latitude']}\n"
                     f"Longitude: {weather['longitude']}\n")
        else:
           print("Warning", "Please enter a city name.")

display_weather()


