def get_unique_categories(data):
    # Initialize a set to store unique categories
    categories = set()

    # Loop through each row in the data
    for row in data:
        # Loop through each category in the row and add to the set
        for category in row:
            categories.add(category)

    # Convert the set to a sorted list and return
    unique_categories = sorted(list(categories))
    return unique_categories


def one_hot_encode(data, unique_categories):
    # Initialize an empty list to store the one-hot encoded data
    one_hot_encoded_data = []

    # Loop through each row in the data
    for row in data:
        # Initialize an empty list for the encoded row
        encoded_row = [1 if category in row else 0 for category in unique_categories]
        # Append the encoded row to the one-hot encoded data list
        one_hot_encoded_data.append(encoded_row)

    return one_hot_encoded_data


# Call the main function to execute the code
if __name__ == "__main__":
    # Input data
    data = [['red', 'blue'], ['green'], ['blue', 'yellow'], ['red', 'yellow']]

    # Get unique categories
    unique_categories = get_unique_categories(data)

    # Perform one-hot encoding
    one_hot_encoded_data = one_hot_encode(data, unique_categories)

    # Print the one-hot encoded data
    for row in one_hot_encoded_data:
        print(row)
