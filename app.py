import requests
from flask import Flask, render_template


app = Flask(__name__)

CITY_NAME = 'Washington, DC'

def get_weather_data():
    url = f'https://api.open-meteo.com/v1/forecast?latitude=38.9072&longitude=77.0369&hourly=temperature_2m&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

@app.route('/')
def index():
    weather_data = get_weather_data()
    if weather_data:
        current_temp = weather_data['hourly']['temperature_2m'][0]
        return render_template('index.html', current_temp=current_temp)
    else:
        return "Failed to fetch weather data."

if __name__ == '__main__':
    app.run(debug=True)
