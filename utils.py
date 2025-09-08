import requests
import pandas as pd
import matplotlib.pyplot as plt


def graph(weather: pd.DataFrame) -> None:
    df = weather.df()

    plt.plot(df['date'], df['temp'])
    plt.title('temperature graph')
    plt.xlabel('date')
    plt.ylabel('temperature in °C')
    plt.legend(loc='lower right')
    plt.show()



def get_weather(location: tuple[float, float], dates: tuple[str, str]) -> pd.DataFrame:
    era = 5
    base_url = f"https://archive-api.open-meteo.com/v1/era{era}"
    response = requests.get(base_url, params={
        "latitude": location[0],
        "longitude": location[1],
        "start_date": dates[0],
        "end_date": dates[1],
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