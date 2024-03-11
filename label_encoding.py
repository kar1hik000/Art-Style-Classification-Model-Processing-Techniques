def label_encode_categorical(data):
    # Initialize an empty dictionary to store label mappings
    label_mapping = {}
    
    # Initialize an empty list to store encoded data
    encoded_data = []
    
    # Find unique values in the data
    unique_values = set(data)
    
    # Create a label mapping for each unique value
    for i, value in enumerate(unique_values):
        label_mapping[value] = i
    
    # Encode each value in the data using the label mapping
    for value in data:
        encoded_data.append(label_mapping[value])
    
    return encoded_data, label_mapping

if __name__ == "__main__":
    # Sample categorical data
    categorical_data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    
    # Perform label encoding
    encoded_data, label_mapping = label_encode_categorical(categorical_data)
    
    # Print the encoded data and label mapping
    print("Encoded Data:", encoded_data)
    print("Label Mapping:", label_mapping)
