def prefix_product(A):
    n = len(A)
    B = [1] * n  # Initialize B with 1s

    for i in range(n):
        for j in range(i + 1):  # j goes from 0 to i (Python uses zero-based indexing)
            B[i] *= A[j]
    
    return B

# Example usage
A = [5, 2, 2]
B = prefix_product(A)
print(B)  # Output: [2, 6, 24]
