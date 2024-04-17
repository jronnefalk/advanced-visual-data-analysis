import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("Data/EyeTrack-raw.tsv", delimiter="\t")

# Print the first few rows to check the data
# print(data.head())

# Plotting the data for gazepoints in x and y
plt.scatter(data["GazePointX(px)"], data["GazePointY(px)"])
plt.xlabel("X coordinate of gaze point in pixels")
plt.ylabel("Y coordinate of gaze point in pixels")
plt.show()

# Scatter plot with adjusted alpha
plt.scatter(data["GazePointX(px)"], data["GazePointY(px)"], alpha=0.25)
plt.xlabel("X coordinate of gaze point in pixels")
plt.ylabel("Y coordinate of gaze point in pixels")
plt.show()


# Normalize the gaze duration for visibility
data["NormalizedDuration"] = (
    data["GazeEventDuration(mS)"] / data["GazeEventDuration(mS)"].max()
)

# Apply linear scaling with a controlled minimum size
data["PointSizes"] = (
    data["NormalizedDuration"] * 500
)  # Scale factor adjusted for visibility
data["PointSizes"] = data["PointSizes"].apply(
    lambda x: max(x, 10)
)  # Set a minimum size

# Scatter plot where the size of each point is based on the linearly scaled gaze duration
plt.scatter(
    data["GazePointX(px)"],
    data["GazePointY(px)"],
    alpha=0.25,
    s=data["PointSizes"],
)
plt.xlabel("X coordinate of gaze point in pixels")
plt.ylabel("Y coordinate of gaze point in pixels")
plt.show()
