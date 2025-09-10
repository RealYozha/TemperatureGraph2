from os import getenv
from dotenv import load_dotenv
import requests
import matplotlib.pyplot as plt
import pandas as pd


def graph(weather: pd.DataFrame) -> None:
    df = weather.df()

    plt.plot(df['date'], df['temp'])
    plt.title('temperature graph')
    plt.xlabel('date')
    plt.ylabel('temperature in °C')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()



def get_weather(location: tuple[float, float], start_date: str, end_date: str) -> pd.DataFrame:
    era = 5
    base_url = f"https://archive-api.open-meteo.com/v1/era{era}"
    response = requests.get(base_url, params={
        "latitude": location[0],
        "longitude": location[1],
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "temperature_2m"
    })
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(list(zip(data['hourly']['time'], data['hourly']['temperature_2m'])), columns=['date', 'temp'])


def get_coords(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lat, lon # latitude, longitude


def main():
    # country_code = "RU"
    yandex_apikey = getenv("YANDEX_GEOCODER_APIKEY")
    city_name = "Saint Petersburg"
    start_date = "2025-08-01"
    end_date = "2025-09-01"

    point = get_coords(yandex_apikey, city_name)
    weather = get_weather(point, start_date, end_date)

    graph(weather)


if __name__ == '__main__':
    load_dotenv()
    main()