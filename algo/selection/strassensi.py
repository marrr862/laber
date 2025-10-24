import numpy as np

def strassen(A, B, depth=0, min_size=64):
    
    indent = "  " * depth
    n = len(A)
    if n <= min_size:
        print(f"{indent}Base case: Using naive multiplication for {n}x{n} matrices")
        return naive_matrix_multiply(A, B)
    
    print(f"{indent}Strassen recursion depth {depth}: {n}x{n} matrices")
    
    
    mid = n // 2
    
    
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
   
    print(f"{indent}Calculating 7 Strassen products:")
    
  
    print(f"{indent}  M1 = (A11 + A22) × (B11 + B22)")
    A11_plus_A22 = add_matrices(A11, A22)
    B11_plus_B22 = add_matrices(B11, B22)
    M1 = strassen_matrix_multiply(A11_plus_A22, B11_plus_B22, depth + 1, min_size)
    
    print(f"{indent}  M2 = (A21 + A22) × B11")
    A21_plus_A22 = add_matrices(A21, A22)
    M2 = strassen_matrix_multiply(A21_plus_A22, B11, depth + 1, min_size)
    
    
    print(f"{indent}  M3 = A11 × (B12 - B22)")
    B12_minus_B22 = subtract_matrices(B12, B22)
    M3 = strassen_matrix_multiply(A11, B12_minus_B22, depth + 1, min_size)
    
    
    print(f"{indent}  M4 = A22 × (B21 - B11)")
    B21_minus_B11 = subtract_matrices(B21, B11)
    M4 = strassen_matrix_multiply(A22, B21_minus_B11, depth + 1, min_size)
    
    
    print(f"{indent}  M5 = (A11 + A12) × B22")
    A11_plus_A12 = add_matrices(A11, A12)
    M5 = strassen_matrix_multiply(A11_plus_A12, B22, depth + 1, min_size)
    
    
    print(f"{indent}  M6 = (A21 - A11) × (B11 + B12)")
    A21_minus_A11 = subtract_matrices(A21, A11)
    B11_plus_B12 = add_matrices(B11, B12)
    M6 = strassen_matrix_multiply(A21_minus_A11, B11_plus_B12, depth + 1, min_size)
    
    
    print(f"{indent}  M7 = (A12 - A22) × (B21 + B22)")
    A12_minus_A22 = subtract_matrices(A12, A22)
    B21_plus_B22 = add_matrices(B21, B22)
    M7 = strassen_matrix_multiply(A12_minus_A22, B21_plus_B22, depth + 1, min_size)
    
   
    print(f"{indent}Combining results:")
    
    
    C11 = add_matrices(M1, M4)
    C11 = subtract_matrices(C11, M5)
    C11 = add_matrices(C11, M7)
    
    
    C12 = add_matrices(M3, M5)
    
    
    C21 = add_matrices(M2, M4)
    
    
    C22 = subtract_matrices(M1, M2)
    C22 = add_matrices(C22, M3)
    C22 = add_matrices(C22, M6)
    
    
    result = combine_quarters(C11, C12, C21, C22)
    
    print(f"{indent}Completed {n}x{n} multiplication")
    return result


def naive(A, B):
    
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def add_matrices(A, B):
    
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def subtract_matrices(A, B):
    
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def combine_quarters(C11, C12, C21, C22):
    
    n = len(C11)
    result = []
    
    
    for i in range(n):
        result.append(C11[i] + C12[i])
    
    
    for i in range(n):
        result.append(C21[i] + C22[i])
    
    return result

def print_matrix(matrix, name="Matrix"):
    
    print(f"{name}:")
    for row in matrix:
        print("  [" + " ".join(f"{x:3}" for x in row) + "]")
    print()

def d_strassen():
    
    print("Strassen's Algorithm ")
    print("=" * 50)
    
    
    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    B = [
        [16, 15, 14, 13],
        [12, 11, 10, 9],
        [8, 7, 6, 5],
        [4, 3, 2, 1]
    ]
    
    print("Input Matrices:")
    print_matrix(A, "A")
    print_matrix(B, "B")
    
    print("Strassen :")
    print("-" * 40)
    
    result = strassen(A, B, min_size=2)
    
    print("\nFinal Result:")
    print_matrix(result, "A × B (Strassen)")
    
    
    naive_result = naive(A, B)
    print("Verification (Naive Multiplication):")
    print_matrix(naive_result, "A × B (Naive)")
    
    
    is_correct = all(
        result[i][j] == naive_result[i][j] 
        for i in range(len(A)) 
        for j in range(len(B[0]))
    )
    print(f"Results match: {is_correct}")

d_strassen()
