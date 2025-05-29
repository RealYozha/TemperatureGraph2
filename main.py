from os import getenv
from dotenv import load_dotenv
from weather import get_weather
from geoPoint import get_coords
from graph import graph


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
# ! THE ABOVE CODE DOESN'T WORK FOR ME, IT WORKS FOR MY COACH THOUGH FOR SOME REASON


def main():
    # country_code = "RU"
    yandex_apikey = getenv("YANDEX_GEOCODER_APIKEY")
    city_name = "Saint Petersburg"
    date_range = ("2025-04-01", "2025-05-01")

    point = get_coords(yandex_apikey, city_name)
    weather = get_weather(point, date_range)

    graph(weather)


if __name__ == '__main__':
    load_dotenv()
    main()