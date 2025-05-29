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
