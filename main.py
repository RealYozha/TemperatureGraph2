from os import getenv
from dotenv import load_dotenv
from geoPoint import Point
from weather import Weather
from daterange import DateRange
from graph import Graph


# def get_coords(city, country_code):
#     url = "https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-postal-code@public/records"
#     params = {
#         "where": f"place_name='{city}' AND country_code='{country_code}'",
#         "limit": 1,
#         "select": "latitude,longitude"
#     }
#     response = requests.get(url, params=params)
#     response.raise_for_status()
#     return response.json()


def main():
    # country_code = "RU"
    yandex_apikey = getenv("YANDEX_GEOCODER_APIKEY")
    city_name = "Saint Petersburg"
    date_range = DateRange("2025-04-01", "2025-05-01")

    point = Point(yandex_apikey, city_name)
    weather = Weather(point, date_range)

    graph = Graph(weather)


if __name__ == '__main__':
    load_dotenv()
    main()