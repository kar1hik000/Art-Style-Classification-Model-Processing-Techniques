def matrix_multiply(A, B):
    # Check if the number of columns in A matches the number of rows in B for matrix multiplication
    if len(A[0]) != len(B):
        return None

    # Initialize the result matrix with zeros
    result = [[0] * len(B[0]) for _ in range(len(A))]

    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


def input_matrix(rows, cols, name):
    matrix = []
    print(f"For Matrix {name}")
    print("Enter the entries row-wise:")

    # Loop to get user input for each row and column
    for i in range(rows):
        a = []
        for j in range(cols):
            a.append(int(input()))
        matrix.append(a)
    return matrix


if __name__ == "__main__":
    # Get user input for matrix A
    rows_A = int(input("Enter the number of rows for matrix A: "))
    cols_A = int(input("Enter the number of columns for matrix A: "))
    matrix_A = input_matrix(rows_A, cols_A, "A")

    # Get user input for matrix B
    rows_B = int(input("Enter the number of rows for matrix B: "))
    cols_B = int(input("Enter the number of columns for matrix B: "))
    matrix_B = input_matrix(rows_B, cols_B, "B")

    # Multiply matrices A and B
    result_matrix = matrix_multiply(matrix_A, matrix_B)

    # Check if multiplication was successful and print the result
    if result_matrix is not None:
        print("Matrix A * Matrix B:")
        for row in result_matrix:
            print(row)
    else:
        print("Error: Matrices A and B are not multipliable.")
