import ephem

def get_sun_times_for_cities():
    # List of cities with latitude and longitude
    cities = [
        {"name": "New Delhi", "lat": "28.6139", "lon": "77.2090"},
        {"name": "New York", "lat": "40.7128", "lon": "-74.0060"},
        {"name": "Tokyo", "lat": "35.6895", "lon": "139.6917"},
        {"name": "London", "lat": "51.5074", "lon": "-0.1278"},
        {"name": "Sydney", "lat": "-33.8688", "lon": "151.2093"}
    ]
    # Get current date and time
    current_date = ephem.now()

    print(f"Current Date: {current_date}\n")
    print(f"{'City':<15} {'Next Sunrise':<20} {'Next Sunset':<20}")
    print("-" * 55)

    # Loop through each city and calculate sun times
    for city in cities:
        observer = ephem.Observer()
        observer.lat = city["lat"]
        observer.lon = city["lon"]
        observer.date = current_date

        # Calculate sunrise and sunset
        sunrise = observer.next_rising(ephem.Sun())
        sunset = observer.next_setting(ephem.Sun())

        # Display results for the city
        print(f"{city['name']:<15} {str(sunrise):<20} {str(sunset):<20}")

print("Welcome to The Cosmic Sunrise and Sunset Tracker!")
get_sun_times_for_cities()


