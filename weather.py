from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
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
            'humidity': weather_data['main']['humidity']
        }
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to get weather data: {e}")
        return None
class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Weather App")
        self.root.geometry("500x500")
        self.image = Image.open("D:\climate.png") 
        # Change the filename to your image file
        self.photo = ImageTk.PhotoImage(self.image)
        # Create a label to hold the image
        self.image_label = Label(root, image=self.photo)
        self.image_label.pack(pady=5)
        self.city_label = Label(self.root, text="City:")
        self.city_label.pack(pady=10)
        self.city_entry = Entry(self.root)
        self.city_entry.pack(pady=10)
        self.get_weather_button = Button(
            self.root, text="Get Weather", command=self.display_weather )
        self.get_weather_button.pack(pady=10)
        self.result_label = Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def display_weather(self):
        city = self.city_entry.get()
        if city:
            weather = get_weather(city)
            if weather:
                self.result_label.config(text=f"City: {weather['city']}\n"
                                              f"Temperature: {weather['temperature']}°C\n"
                                              f"Description: {weather['description']}\n"
                                              f"Humidity: {weather['humidity']}%")
        else:
            messagebox.showwarning("Warning", "Please enter a city name.")

if __name__ == "__main__":
    root = Tk()
    app = WeatherApp(root)
    root.mainloop()
