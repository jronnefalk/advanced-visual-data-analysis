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
plt.xlabel("X Coordinate (pixels)")
plt.ylabel("Y Coordinate (pixels)")
plt.title("Visualization of Gaze Points")
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

