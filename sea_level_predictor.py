import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line of best fit (all data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = np.arange(1880, 2051)
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, color='red')

    # Line of best fit (2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = np.arange(2000, 2051)
    y_pred2 = res2.intercept + res2.slope * x_pred2
    plt.plot(x_pred2, y_pred2, color='green')

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot
    plt.savefig("sea_level_plot.png")

    return plt.gca()
