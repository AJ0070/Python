def determinant(matrix):
    # Calculate the determinant of a 3x3 matrix.
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    return det

def transpose(matrix):
    # Transpose a 3x3 matrix.
    return [[matrix[j][i] for j in range(3)] for i in range(3)]

def cofactor(matrix):
    # Calculate the cofactor matrix of a 3x3 matrix.
    cofactor_matrix = []
    for i in range(3):
        cofactor_row = []
        for j in range(3):
            minor_matrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            sign = (-1) ** (i + j)
            cofactor_row.append(sign * determinant(minor_matrix))
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix

def inverse(matrix):
    # Calculate the inverse of a 3x3 matrix.
    det = determinant(matrix)
    if det == 0:
        raise ValueError("The matrix is singular and does not have an inverse.")
    
    cofactor_matrix = cofactor(matrix)
    adjugate_matrix = transpose(cofactor_matrix)
    
    inverse_matrix = [[adjugate_matrix[i][j] / det for j in range(3)] for i in range(3)]
    
    return inverse_matrix

def input_matrix():
    # Ask the user for a matrix input.
    num_rows = int(input("Enter the number of rows: "))
    num_cols = int(input("Enter the number of columns: "))
    
    matrix = []
    print(f"Enter a {num_rows}x{num_cols} matrix:")
    
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            value = float(input(f"Enter the value at row {i + 1}, column {j + 1}: "))
            row.append(value)
        matrix.append(row)
    
    return matrix

def main():
    try:
        matrix = input_matrix()
        inverse_matrix = inverse(matrix)
        print("Inverse matrix:")
        for row in inverse_matrix:
            print(row)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
