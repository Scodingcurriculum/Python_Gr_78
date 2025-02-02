from tkinter import *
from tkinter import scrolledtext
import requests

# Function to get news
def get_news():
    api_key = 'a74543bdf472441f9d9af601a969ae13'  # Replace with your NewsAPI key
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    
    response = requests.get(url)
    news_data = response.json()

    news_text.delete(1.0,  END)  # Clear the existing content
    
    if news_data['status'] == 'ok':
        for article in news_data['articles']:
            title = article['title']
            description = article['description']
            url = article['url']
            news_text.insert( END, f"Title: {title}\n")
            news_text.insert( END, f"Description: {description}\n")
            news_text.insert( END, f"Read more: {url}\n\n")
    else:
        news_text.insert( END, "Failed to fetch news.")

# Setting up the Tkinter root
root =  Tk()
root.title("Live News App")
root.geometry("800x600")

# Create a ScrolledText widget
news_text = scrolledtext.ScrolledText(root, wrap= WORD, width=100, height=30, font=("Arial", 12))
news_text.pack(padx=10, pady=10)

# Create a refresh button
refresh_button =  Button(root, text="Refresh News", command=get_news, font=("Arial", 14))
refresh_button.pack(pady=10)

# Fetch news initially
get_news()

# Start the Tkinter event loop
root.mainloop()
