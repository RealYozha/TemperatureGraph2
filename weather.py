import requests
import pandas as pd


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
    self.data = response.json()
    return pd.DataFrame(list(zip(self.data['hourly']['time'], self.data['hourly']['temperature_2m'])), columns=['date', 'temp'])
