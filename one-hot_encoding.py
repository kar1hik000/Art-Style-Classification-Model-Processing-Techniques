def one_hot_encoding(data):

    one_hot_encoded = []

    categories = set()

    for row in data:
        for category in row:
            categories.add(category)

    categories = sorted(list(categories))

    for row in data:

        encoded_row = []

        for category in categories:
            if category in row:
                encoded_row.append(1)
            else:
                encoded_row.append(0)
        one_hot_encoded.append(encoded_row)

    return one_hot_encoded

data = [['red', 'blue'], ['green'], ['blue', 'yellow'], ['red', 'yellow']]
one_hot_encoded_data = one_hot_encoding(data)
print(one_hot_encoded_data)
