import os
import requests
import csv
from datetime import datetime

if os.name == "nt":
    from dotenv import load_dotenv

    load_dotenv()


def get_api_key():
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
    if not api_key:
        raise ValueError("OpenWeatherMap API key not found in environment variables.")
    return api_key


def get_weather(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    temperature = data["main"]["temp"]
    weather_description = data["weather"][0]["description"]

    return temperature, weather_description


def update_csv(file_path, lat, lon, api_key):
    temperature, weather_description = get_weather(api_key, lat, lon)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        # csv_writer.writerow([timestamp, lat, lon, temperature, weather_description])
        csv_writer.writerow([timestamp, temperature, weather_description])


if __name__ == "__main__":
    api_key = get_api_key()
    lat, lon = [41.6941, 44.8337]
    file_path = "weather_data.csv"

    update_csv(file_path, lat, lon, api_key)
