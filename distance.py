import numpy as np
from collections import Counter

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def k_nearest_neighbors(training_data, training_labels, test_instance, k=3):
    distances = [euclidean_distance(test_instance, instance) for instance in training_data]
    k_nearest_indices = np.argsort(distances)[:k]
    k_nearest_labels = [training_labels[i] for i in k_nearest_indices]
    most_common_label = Counter(k_nearest_labels).most_common(1)
    return most_common_label[0][0]

# Example usage with changed variable names:
training_data = np.array([[1, 2], [2, 3], [3, 1], [4, 2]])
training_labels = np.array([0, 0, 1, 1])

test_instance = np.array([2.5, 2])
k_value = 2

predicted_label = k_nearest_neighbors(training_data, training_labels, test_instance, k=k_value)
print(f"The predicted label for the test instance is: {predicted_label}")
