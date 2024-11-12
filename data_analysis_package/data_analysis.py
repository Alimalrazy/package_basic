import pandas as pd
import numpy as np

def calculate_statistics(df):
    """Calculates basic statistics for the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.

    Returns:
        tuple: A tuple containing the mean and standard deviation.
    """

    mean = df.mean()
    std_dev = df.std()

    return mean, std_dev