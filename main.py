import pandas as pd
import data_analysis_package.data_cleaning as dc
import data_analysis_package.data_analysis as da
import data_analysis_package.data_visualization as dv

print("Modules imported successfully.")

# Load data
df = pd.read_csv('Pizza_price.csv')
print("Data loaded successfully.")

# Clean data
cleaned_df = dc.clean_data(df)
print("Data cleaned successfully.")

# Analyze data
mean, std_dev = da.calculate_statistics(cleaned_df)
print("Statistics calculated successfully.")
print("Mean:", mean)
print("Standard Deviation:", std_dev)

# Visualize data
dv.plot_histogram(cleaned_df, 'price')
print("Histogram plotted successfully.")