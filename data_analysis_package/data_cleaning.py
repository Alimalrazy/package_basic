import pandas as pd

def clean_data(df):
    """Cleans the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to clean.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """

    # Handle missing values (replace with forward fill)
    df.fillna(method='ffill', inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    return df