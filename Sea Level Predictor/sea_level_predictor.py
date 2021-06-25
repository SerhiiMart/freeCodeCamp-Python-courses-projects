import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision='legacy')

    
    # Create scatter plot
    y = df["CSIRO Adjusted Sea Level"]
    x = df["Year"]
    plt.scatter(x, y, data=df)
    fig, ax = plt.subplots()

    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()