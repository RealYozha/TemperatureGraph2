import pandas as pd
from weather import Weather
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, weather: Weather) -> None:
        df = weather.df()

        plt.plot(df['date'], df['temp'])
        plt.title('temperature graph')
        plt.xlabel('date')
        plt.ylabel('temperature in °C')
        plt.legend(loc='lower right')
        plt.show()
