def matrix(A, B):
    
    m = len(A)
    n = len(A[0])
    p = len(B[0])   
    if len(B) != n:
        raise ValueError(f"Cannot multiply {m}x{n} matrix with {len(B)}x{p} matrix")
    
    print(f"Multiplying {m}x{n} matrix with {n}x{p} matrix")
    print(f"Result will be {m}x{p} matrix")
    print()
       
    C = [[0 for _ in range(p)] for _ in range(m)]   
    for i in range(m):
        print(f"Processing row {i}: {A[i]}")
        for j in range(p):
            print(f"  Column {j}: ", end="")
            dot_product = 0
            calculation_steps = []
            
            for k in range(n):
                product = A[i][k] * B[k][j]
                dot_product += product
                calculation_steps.append(f"{A[i][k]}×{B[k][j]}")            
            C[i][j] = dot_product
            print(f" {' + '.join(calculation_steps)} = {dot_product}")    
    return C


def orinak():
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    
    print("Naive Matrix Multiplication")
    print("=" * 50)
    print("Matrix A (2x3):")
    for row in A:
        print(f"  {row}")
    
    print("\nMatrix B (3x2):")
    for row in B:
        print(f"  {row}")
    
    print("\nMultiplication Process:")
    print("-" * 30)
    
    result = matrix(A, B)
    
    print("\nResult Matrix C (2x2):")
    for row in result:
        print(f"  {row}")
orinak()
