import requests


class Point:
    def __init__(self, apikey: str, address: str) -> None:
        self.apikey = apikey

        base_url = "https://geocode-maps.yandex.ru/1.x"
        response = requests.get(base_url, params={
            "geocode": address,
            "apikey": self.apikey,
            "format": "json",
        })
        response.raise_for_status()
        found_places = response.json()['response']['GeoObjectCollection']['featureMember']

        if not found_places:
            return None

        most_relevant = found_places[0]
        lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
        self.lat, self.lon = lat, lon # latitude, longitude
    
    def unpack(self) -> tuple[float, float]:
        return self.lat, self.lon