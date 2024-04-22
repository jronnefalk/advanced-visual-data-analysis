import cv2
import numpy as np
import os
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt


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


def extract_features(images):
    feature_vectors = []
    for img in images:
        features = []
        # 1. Colour content
        mean_r = np.mean(img[:, :, 2])
        mean_g = np.mean(img[:, :, 1])
        mean_b = np.mean(img[:, :, 0])
        features.extend([mean_r, mean_g, mean_b])

        # 2. Colour distribution around the central point
        h, w = img.shape[:2]
        center = (w // 2, h // 2)
        central_region = img[
            center[1] - 10 : center[1] + 10, center[0] - 10 : center[0] + 10
        ]
        mean_central = cv2.mean(central_region)[:3]
        features.extend(mean_central)

        # 3. Colour distribution around several points
        points = [
            (w // 4, h // 4),
            (3 * w // 4, h // 4),
            (w // 4, 3 * h // 4),
            (3 * w // 4, 3 * h // 4),
        ]  # corners
        for x, y in points:
            color_region = img[y - 10 : y + 10, x - 10 : x + 10]
            mean_point = cv2.mean(color_region)[:3]
            features.extend(mean_point)

        # 4. Luminance distribution
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for x, y in points:
            gray_region = gray[y - 10 : y + 10, x - 10 : x + 10]
            luminance_mean = np.mean(gray_region)
            features.append(luminance_mean)

        # 5. Edge positions and orientations
        edges = cv2.Canny(img, 100, 200)
        edge_count = np.sum(edges > 0)
        features.append(edge_count)

        feature_vectors.append(features)
    return feature_vectors


# Load images
folder_path = "Labb 3\images"
images, filenames = load_images_from_folder(folder_path)

# Extract comprehensive feature vectors
feature_vectors = extract_features(images)

# Display feature vectors
# for filename, feature_vector in zip(filenames, feature_vectors):
#     print(f"{filename}: Feature Vector = {feature_vector}")

# Compare image 04.jpg to others
reference_idx = filenames.index("04.jpg")
reference_vector = feature_vectors[reference_idx]

distances = [
    np.linalg.norm(np.array(reference_vector) - np.array(fv)) for fv in feature_vectors
]
sorted_indices = np.argsort(distances)

print("\nImages ranked by similarity to '04.jpg':")
for idx in sorted_indices:
    print(f"{filenames[idx]} with distance {distances[idx]}")

# Extract comprehensive feature vectors
feature_vectors = extract_features(images)

# Create a distance matrix
dist_matrix = distance_matrix(feature_vectors, feature_vectors)

# Plot distance matrix as an image with annotated axes
plt.imshow(dist_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Distance')
plt.title('Distance Matrix')
plt.xlabel('Image Index')
plt.ylabel('Image Index')
plt.xticks(ticks=np.arange(len(filenames)), labels=filenames, rotation=90)
plt.yticks(ticks=np.arange(len(filenames)), labels=filenames)
plt.show()