

# Input Matrices
A = [[5,6],
     [7,8]]

B = [[1,2],
    [3,4]]

print("Matrix A:")
for row in A:
    print(row)

print("Matrix B:")
for row in B:
    print(row)

# 1. Addition
add = [[0,0],
       [0,0]]

for i in range(2):
    for j in range(2):
        add[i][j] = A[i][j] + B[i][j]

print("\nAddition of Two Matrices:")
for row in add:
    print(row)

#2. Subtraction
sub = [[0,0],
       [0,0]]

for i in range(2):
    for j in range(2):
        sub[i][j] = A[i][j] - B[i][j]

print("\nSubtraction of Two Matrices:")
for row in sub:
    print(row)

#3.Multiplication
multiply = [[0,0],
            [0,0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            multiply[i][j] = A[i][k] * B[k][j]
print("\nMultiplication of Two Matrice:")
for row in multiply:
    print(row)

# 4. Transpose
transpose_A = [[0,0],
               [0,0]]
for i in range(2):
    for j in range(2):
        transpose_A[j][i] = A[i][j]
print("\n The Transpose of Matrix A is :")
for row in transpose_A:
    print(row)

#5. Determinant
# |A| = ad-bc
det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0]
print("\n The Determinant of Matrix A is :")
print(det_A)
# determinant = a single numeric value calculated from a square matrix used to check matrix have inverse or not ,to solve linear equations and used in graphics,AI,ML,engineering
#matrix is a box of number and determinant is the value of that box



