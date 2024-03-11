import numpy as np
from collections import Counter

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


def k_nearest_neighbors(training_data, training_labels, test_instance, k=3):
    # Calculate distances between test instance and all training data points
    distances = [euclidean_distance(test_instance, instance) for instance in training_data]

    # Get the indices of the k nearest neighbors
    k_nearest_indices = np.argsort(distances)[:k]

    # Get the labels of the k nearest neighbors
    k_nearest_labels = [training_labels[i] for i in k_nearest_indices]

    # Find the most common label among the k nearest neighbors
    most_common_label = Counter(k_nearest_labels).most_common(1)

    return most_common_label[0][0]


if __name__ == "__main__":
    # Sample training data and labels
    training_data = np.array([[1, 2], [2, 3], [3, 1], [4, 2]])
    training_labels = np.array([0, 0, 1, 1])

    # Test instance for prediction
    test_instance = np.array([2.5, 2])
    
    # Value of k for k-nearest neighbors
    k_value = 2

    # Predict the label for the test instance using k-nearest neighbors
    predicted_label = k_nearest_neighbors(training_data, training_labels, test_instance, k=k_value)

    # Print the predicted label for the test instance
    print(f"The predicted label for the test instance is: {predicted_label}")
