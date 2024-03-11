def get_matrix_input():
    # Get the number of rows and columns for the matrix
    num_rows = int(input("Enter the number of rows in the matrix: "))
    num_cols = int(input("Enter the number of columns in the matrix: "))

    matrix = []

    # Loop to get user input for each element in the matrix
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    return matrix


def transpose_matrix(matrix):
    # Using the zip function to transpose the matrix
    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix


if __name__ == "__main__":
    # Getting matrix input from the user
    input_matrix = get_matrix_input()

    # Transposing the matrix
    transposed_result = transpose_matrix(input_matrix)

    # Printing original matrix
    print("\nOriginal Matrix:")
    for row in input_matrix:
        print(row)

    # Printing transposed matrix
    print("\nTransposed Matrix:")
    for row in transposed_result:
        print(row)
