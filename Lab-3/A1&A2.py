import numpy as np
import pandas as pd

def read_excel_data(file_name, sheet_name):
    df = pd.read_excel(file_name, sheet_name=sheet_name)
    return df

def calculate_cost_per_product(data_frame):
    A = data_frame.iloc[:, 1:4]
    C = data_frame.iloc[:, 4]
    A_pseudo_inverse = np.linalg.pinv(A)
    cost_per_product = np.dot(A_pseudo_inverse, C)
    return cost_per_product

if __name__ == "__main__":
    # Read Excel data
    df = read_excel_data('Lab Session1 Data.xlsx', sheet_name='Purchase data')
    
    # Calculate properties
    dimensionality = df.shape[1] - 1  # Excluding the first column which might be an index
    num_vectors = df.shape[0]
    rank_A = np.linalg.matrix_rank(df.iloc[:, 1:4])  # Rank of columns 1 to 3
    
    # Calculate cost per product
    cost_per_product = calculate_cost_per_product(df)
    
    # Print results
    print("Dimensionality of the vector space:", dimensionality)
    print("Number of vectors in the vector space:", num_vectors)
    print("Rank of Matrix A:", rank_A)
    print("Cost of each product using Pseudo-Inverse:")
    print(cost_per_product)

