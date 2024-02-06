def label_encode_categorical(data):

    label_mapping = {}
    encoded_data = []

    unique_values = set(data)
    for i, value in enumerate(unique_values):

        label_mapping[value] = i

    for value in data:
        encoded_data.append(label_mapping[value])

    return encoded_data, label_mapping

categorical_data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
encoded_data, label_mapping = label_encode_categorical(categorical_data)
print("Encoded Data:", encoded_data)
print("Label Mapping:", label_mapping)
