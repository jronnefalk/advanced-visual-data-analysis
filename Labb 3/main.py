import cv2
import numpy as np
import os
from scipy.spatial import distance_matrix


# Function to load images from a directory
def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        if filename.endswith(".png"):  # Assuming all images are in PNG format
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
                filenames.append(filename)
    return images, filenames
