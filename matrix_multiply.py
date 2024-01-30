def matrix_multiply(A, B):

    if len(A[0]) != len(B):
        return None

    result = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


def input_matrix(rows, cols, name):

 matrix = []
 print("For Matrix",name)
 print("Enter the entries rowwise:")
 
 for i in range(rows):          
    a =[]
    for j in range(cols):      
         a.append(int(input()))
    matrix.append(a)
 return matrix 

if __name__ == "__main__":

    rows_A = int(input("Enter the number of rows for matrix A: "))
    cols_A = int(input("Enter the number of columns for matrix A: "))
    matrix_A = input_matrix(rows_A, cols_A, "A")

    rows_B = int(input("Enter the number of rows for matrix B: "))
    cols_B = int(input("Enter the number of columns for matrix B: "))
    matrix_B = input_matrix(rows_B, cols_B, "B")

    result_matrix = matrix_multiply(matrix_A, matrix_B)

    if result_matrix is not None:
        print("Matrix A * Matrix B:")
        for row in result_matrix:
            print(row)
    else:
        print("Error: Matrices A and B are not multipliable.")
