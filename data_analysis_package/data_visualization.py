import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    """Plots a histogram for the specified column.

    Args:
        df (pd.DataFrame): The DataFrame to plot.
        column (str): The column name to plot.
    """

    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()