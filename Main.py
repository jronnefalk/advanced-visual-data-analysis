import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


data = pd.read_csv("Data/EyeTrack-raw.tsv", delimiter="\t")

# Print the first few rows to check the data
# print(data.head())

# Plotting the data for gazepoints in x and y
plt.scatter(data["GazePointX(px)"], data["GazePointY(px)"])
plt.xlabel("X Coordinate (pixels)")
plt.ylabel("Y Coordinate (pixels)")
plt.title("Visualization of Gaze Points")
plt.show()


# Assuming you decide to find, e.g., 5 clusters
kmeans = KMeans(n_clusters=4)
data["cluster"] = kmeans.fit_predict(data[["GazePointX(px)", "GazePointY(px)"]])

# Plotting clusters
plt.scatter(
    data["GazePointX(px)"], data["GazePointY(px)"], c=data["cluster"], cmap="viridis"
)
plt.xlabel("X Coordinate (pixels)")
plt.ylabel("Y Coordinate (pixels)")
plt.title("Clustered Gaze Points")
plt.colorbar(label="Cluster")
plt.show()
