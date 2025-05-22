import requests
from geoPoint import Point
from daterange import DateRange
import pandas as pd


class Weather:
    def __init__(self, point: Point, date_range: DateRange) -> None:
        location = point.unpack()
        dates = date_range.unpack()

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
    
    def df(self) -> pd.DataFrame:
        return pd.DataFrame(list(zip(self.data['hourly']['time'], self.data['hourly']['temperature_2m'])), columns=['date', 'temp'])
