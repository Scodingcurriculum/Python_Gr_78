import ephem
from datetime import datetime
def get_sorted_sun_times(sort_by):
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
    city_sun_times = []
    # Loop through each city and calculate sun times
    for city in cities:
        observer = ephem.Observer()
        observer.lat = city["lat"]
        observer.lon = city["lon"]
        observer.date = current_date
        # Calculate sunrise and sunset
        sunrise = observer.next_rising(ephem.Sun())
        sunset = observer.next_setting(ephem.Sun())
        # Collect data for sorting
        city_sun_times.append({
            "name": city["name"],
            "sunrise": datetime.strptime(str(sunrise), "%Y/%m/%d %H:%M:%S"),
            "sunset": datetime.strptime(str(sunset), "%Y/%m/%d %H:%M:%S")
        })
    # Sorting helper function
    def sort_key(city):
        return city[sort_by]
    # Sort based on the selected criterion
    sorted_cities = sorted(city_sun_times, key=sort_key)
    # Display results
    print(f"{'City':<15} {'Next Sunrise':<20} {'Next Sunset':<20}")
    print("-" * 55)
    for city in sorted_cities:
        print(f"{city['name']:<15} {city['sunrise']} {city['sunset']}")

if __name__ == "__main__":
    print("Welcome to the Sunrise and Sunset Sorter!")
    print("Choose how you want to sort the cities:")
    print("1. By Sunrise")
    print("2. By Sunset")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nSorting cities by next sunrise time...\n")
        get_sorted_sun_times("sunrise")
    elif choice == "2":
        print("\nSorting cities by next sunset time...\n")
        get_sorted_sun_times("sunset")
    else:
        print("Invalid choice. Please enter 1 or 2.")
