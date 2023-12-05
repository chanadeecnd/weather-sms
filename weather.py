import json
import requests
# "lat": 13.82535264157781
# "lon": 100.51602189588719


def get_weather(lat, lon, create_file=False):
    api_key = "81b48da06cfcd7f74f2b14bf6ee915f5"
    weatherURL = "https://api.openweathermap.org/data/2.5/weather"
    api_param = {
        "lat": float(lat),
        "lon": float(lon),
        "appid": api_key
    }
    response = requests.get(weatherURL, params=api_param).json()
    weather = response.get("weather")
    if create_file:
        with open(f'response_get_{response.get("name")}.json', 'w', encoding='utf-8') as output_file:
            json.dump(response, output_file, ensure_ascii=False, indent=2)
            print(f"write data to {output_file.name} successfully.")

    return response

