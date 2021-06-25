import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
     # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision='legacy')

    # Create scatter plot
    y = df["CSIRO Adjusted Sea Level"]
    x = df["Year"]
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    x_guess = pd.Series([i for i in range(1880, 2051)])
    y_guess = res.slope*x_guess + res.intercept
    plt.plot(x_guess, y_guess, "r")

    # Create second line of best fit
    latest_df = df.loc[df['Year'] >= 2000]
    latest_x = latest_df['Year']
    latest_y = latest_df["CSIRO Adjusted Sea Level"]
    res_2 = linregress(latest_x, latest_y)
    x_guess2 = pd.Series([i for i in range(2000, 2051)])
    y_guess2 = res_2.slope*x_guess2 + res_2.intercept
    plt.plot(x_guess2, y_guess2, 'green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()