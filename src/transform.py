import pandas as pd


def transform_weather_data(data):
    # Flatten the nested data
    coord = data['coord']
    weather = data['weather'][0]  # Assuming you want the first weather condition
    sys = data['sys']
    main = data['main']
    wind = data['wind']

    # Extract relevant fields and flatten them
    transformed_data = {
        'city': data['name'],
        'coord_lon': coord['lon'],
        'coord_lat': coord['lat'],
        'weather_id': weather['id'],
        'weather_main': weather['main'],
        'weather_description': weather['description'],
        'weather_icon': weather['icon'],
        'base': data['base'],
        'temp': main['temp'],
        'temp_min': main['temp_min'],
        'temp_max': main['temp_max'],
        'pressure': main['pressure'],
        'humidity': main['humidity'],
        'wind_speed': wind['speed'],
        'wind_deg': wind['deg'],
        'clouds_all': data['clouds']['all'],
        'sys_type': sys['type'],
        'sys_country': sys['country'],
        'sys_sunrise': sys['sunrise'],
        'sys_sunset': sys['sunset'],
        'timezone': data['timezone'],
        'id': data['id'],
        'cod': data['cod'],
        'temp_celsius': main['temp'] - 273.15,  # Convert Kelvin to Celsius
        'humidity': main['humidity']
    }

    # Convert to a DataFrame
    df = pd.DataFrame([transformed_data])

    return df


# Example of transforming the data
if __name__ == "__main__":
    data = {
        "coord": {"lon": -0.1257, "lat": 51.5085},
        "weather": [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
        "base": 'stations',
        "main": {'temp': 304.01, 'feels_like': 303.36, 'temp_min': 302.86, 'temp_max': 304.87, 'pressure': 1023,
                 'humidity': 36},
        "visibility": 10000,
        "wind": {'speed': 2.57, 'deg': 0},
        "clouds": {'all': 0},
        "dt": 1750351887,
        "sys": {'type': 2, 'id': 268730, 'country': 'GB', 'sunrise': 1750304568, 'sunset': 1750364456},
        "timezone": 3600,
        "id": 2643743,
        "name": 'London',
        "cod": 200
    }
    df = transform_weather_data(data)
    print(df)
