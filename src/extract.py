import requests
from config.config import API_KEY

def extract_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    return response.json()

# Example of extracting data for a city
if __name__ == "__main__":
    data = extract_weather_data('London')
    print(data)
