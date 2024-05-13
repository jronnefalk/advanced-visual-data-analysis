import pandas as pd
import matplotlib.pyplot as plt

# Load data with error handling
try:
    cc_data = pd.read_csv("MC2/cc_data.csv", encoding="latin1")
    print("Credit card data loaded successfully.")
except UnicodeDecodeError:
    print("Error loading credit card data. Please check the encoding.")

try:
    loyalty_data = pd.read_csv("MC2/loyalty_data.csv", encoding="latin1")
    print("Loyalty card data loaded successfully.")
except UnicodeDecodeError:
    print("Error loading loyalty card data. Please check the encoding.")

# Display the first few rows of the datasets
print(cc_data.head())
print(loyalty_data.head())

# Count the number of transactions at each location for both datasets
cc_location_counts = cc_data["location"].value_counts()
loyalty_location_counts = loyalty_data["location"].value_counts()

# Creating the bar chart
plt.figure(figsize=(12, 8))
# Index alignment for the locations between the two dataframes
all_locations = cc_location_counts.index.union(loyalty_location_counts.index)
cc_location_counts = cc_location_counts.reindex(all_locations, fill_value=0)
loyalty_location_counts = loyalty_location_counts.reindex(all_locations, fill_value=0)

# Plotting both sets of data
bar_width = 0.35  # width of bars

index = range(len(all_locations))
plt.bar(
    index,
    cc_location_counts,
    bar_width,
    label="Credit Card Transactions",
    color="b",
    alpha=0.6,
)
plt.bar(
    [p + bar_width for p in index],
    loyalty_location_counts,
    bar_width,
    label="Loyalty Card Transactions",
    color="r",
    alpha=0.6,
)

plt.xlabel("Locations")
plt.ylabel("Number of Transactions")
plt.title("Number of Transactions at Each Location by Transaction Type")
plt.xticks([p + bar_width / 2 for p in index], all_locations, rotation=45, ha="right")
plt.legend()

plt.tight_layout()
plt.show()
