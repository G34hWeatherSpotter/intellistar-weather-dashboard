from flask import Flask, render_template, send_from_directory
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    city = 'New York'
    weather_data = get_weather(city)
    return render_template('index.html', weather=weather_data)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug=True)
