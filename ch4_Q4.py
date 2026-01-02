# Write a pythonic code to multiply two matrices using nested loops and also perform transpose of the resultant matrix

A = [
    [1,2],
    [3,4]

]
B = [
    [5,6],
    [7,8]
]

# rows_A = len(A)
# cols_A = len(A[0])
# cols_B = len(B[0])
    
# result = [[0 for _ in range(cols_B)]for _ in range(rows_A)]

# for i in range(rows_A):
#     for j in range(cols_B):
#         for k in range(cols_A):
#             result[i][j] += A[i][k] * B[k][j]
# print("Resultant Matrix:")
# for row in result:
#     print(row)

# transpose = [[0 for _ in range(rows_A)] for _ in range(cols_B)]

# for i in range(rows_A):
#     for j in range(cols_B):
#         transpose[j][i] = result[i][j]

# print("\nTranspose of Resultant Matrix:")
# for row in transpose:
#     print(row)

def multiply_matrix(a,b):
    row_a = len(a)
    col_a = len(a[0])
    col_b = len(b[0])
    result = [[0 for _ in range(col_b)]for _ in range(row_a)]
    
    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                result[i][j] += a[i][k] * b[k][j]
    print("Resltant Matrix:")
    for row in result:
        print(row)
    
    transpose = [[0 for _ in range(col_a)]for _ in range(col_b)]

    for i in range (row_a):
        for j in range(col_b):
            transpose[j][i] = result[i][j]
    
    print("\nTranspose of resultant Matrix:")
    for row in transpose:
        print(row)
 



multiply_matrix(A,B)
