import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable


data = pd.read_csv("Data/EyeTrack-raw.tsv", delimiter="\t")


# Step 2: Plotting the scatter plot
plt.figure(figsize=(10, 6))

# Extracting X and Y coordinates and timestamps
x = data['GazePointX(px)']
y = data['GazePointY(px)']
timestamps = data['RecordingTimestamp']
Duration = data['GazeEventDuration(mS)']

# Plotting the data for gazepoints in x and y
plt.scatter(x, y)
plt.xlabel("X coordinate of gaze point in pixels")
plt.ylabel("Y coordinate of gaze point in pixels")
plt.show()

# Scatter plot with adjusted alpha
plt.scatter(x, y, alpha=0.25)
plt.xlabel("X coordinate of gaze point in pixels")
plt.ylabel("Y coordinate of gaze point in pixels")
plt.show()


# Normalize the timestamps for color mapping
norm = Normalize(vmin=timestamps.min(), vmax=timestamps.max())
cmap = plt.get_cmap('viridis')

# Plot each point with a color based on its timestamp
for xi, yi, timestamp in zip(x, y, timestamps):
    color = cmap(norm(timestamp))
    plt.scatter(xi, yi, color=color)

# Adding color bar
sm = ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label('Timestamp')

# Adding labels and title
plt.xlabel('X Coordinate (pixels)')
plt.ylabel('Y Coordinate (pixels)')
plt.title('Scatter Plot of Eye Fixations with Color Coded Timestamps')
plt.show()



# Normalize the timestamps for color mapping
norm = Normalize(vmin=Duration.min(), vmax=Duration.max())
cmap = plt.get_cmap('viridis')

# Plot each point with a color based on its timestamp
for xi, yi, Duration in zip(x, y, Duration):
    color = cmap(norm(Duration))
    plt.scatter(xi, yi, color=color)

# Adding color bar
sm = ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label('Duration time')

# Adding labels and title
plt.xlabel('X Coordinate (pixels)')
plt.ylabel('Y Coordinate (pixels)')
plt.title('Scatter Plot of Eye Fixations with Color Coded Duration time')
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

