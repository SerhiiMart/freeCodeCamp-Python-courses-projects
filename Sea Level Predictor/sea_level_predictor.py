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


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()