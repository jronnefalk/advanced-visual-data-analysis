import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np  # Import numpy for array handling


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


data.sort_values("RecordingTimestamp", inplace=True)

# Normalize and scale the duration for point size
data["ScaledDuration"] = (
    data["GazeEventDuration(mS)"] / data["GazeEventDuration(mS)"].max()
) * 100 + 10

# Setting up the plot
fig, ax = plt.subplots()
scat = ax.scatter(
    [], [], s=[]
)  # Use np.empty with shape (0, 2) to correctly format empty offsets


def init():
    scat.set_offsets(
        np.empty((0, 2))
    )  # Ensure correct dimensionality for empty offsets
    scat.set_sizes(np.array([]))  # Ensure sizes is an empty array
    return (scat,)


# Update function to manage the scatter plot for each frame
def update(frame_number):
    current_data = data[data["RecordingTimestamp"] <= frame_number]
    offsets = current_data[["GazePointX(px)", "GazePointY(px)"]].to_numpy()
    sizes = current_data["ScaledDuration"].to_numpy()
    scat.set_offsets(offsets)
    scat.set_sizes(sizes)
    return (scat,)


# Create the animation
ani = FuncAnimation(
    fig,
    update,
    init_func=init,
    frames=np.arange(
        data["RecordingTimestamp"].min(), data["RecordingTimestamp"].max(), 100
    ),
    blit=True,
    interval=50,
)

plt.show()
