import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Load Data ---
file_name = "Python\src\S_BFI_2_1_modified.csv"
# Assuming the file is a single column with no header based on the data structure
df = pd.read_csv(file_name, header=None)
df.columns = ["Original Data"]
data_series = df["Original Data"]

# --- 2. Define Window Sizes ---
# Short window (W=10): follows the data closely, less smoothing
short_window = 10
# Medium window (W=50): your original specified size
medium_window = 50
# Long window (W=100): highlights the major long-term trend
long_window = 100

# --- 3. Calculate Running Means ---
# The .rolling(window=k).mean() function is the key to efficient calculation
rn_short = data_series.rolling(window=short_window).mean()
rn_medium = data_series.rolling(window=medium_window).mean()
rn_long = data_series.rolling(window=long_window).mean()

# --- 4. Visualization: Comparing Multiple Window Sizes ---

plt.figure(figsize=(12, 6))

# Plot the original data (light gray and thin for context)
plt.plot(
    data_series.index,
    data_series.values,
    label="Original Data",
    color="gray",
    alpha=0.3,
)

# Plot the running means (increasing linewidth for increasing smoothness)
plt.plot(
    rn_short.index,
    rn_short.values,
    label=f"Running Mean (W={short_window})",
    color="orange",
    linewidth=1.5,
)

plt.plot(
    rn_medium.index,
    rn_medium.values,
    label=f"Running Mean (W={medium_window})",
    color="red",
    linewidth=2.5,
)

plt.plot(
    rn_long.index,
    rn_long.values,
    label=f"Running Mean (W={long_window})",
    color="green",
    linewidth=3.0,
)

plt.title("Comparison of Running Means with Different Window Sizes")
plt.xlabel("Data Point Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()  # In a real environment, this displays the plot
# plt.savefig('running_mean_full_comparison_plot.png') # This saves the plot to a file
