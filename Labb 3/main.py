import cv2
import numpy as np
import os
from scipy.spatial import distance_matrix


# Function to load images from a directory
def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        if filename.endswith(".jpg"):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
                filenames.append(filename)
    return images, filenames


# Specify the path to your folder containing images
folder_path = "./images"  # Replace with your actual folder path
loaded_images, loaded_filenames = load_images_from_folder(folder_path)

# Display the filenames of the loaded images
print("Loaded images:")
for filename in loaded_filenames:
    print(filename)
