# matrix-calculator-without-numpy
This project demonstrates basic matrix operations using pure Python without any NumPy built-in functions. It includes addition, subtraction, multiplication, transpose, and determinant of a 2×2 matrix using nested loops and fundamental programming logic. The project helps beginners understand how matrix calculations work internally.

## 📌 Operations Implemented

✔ Matrix Addition  
✔ Matrix Subtraction  
✔ Matrix Multiplication  
✔ Matrix Transpose  
✔ Determinant of 2×2 Matrix  

---

## 🧠 Concept Used

The program uses basic Python programming concepts to perform matrix operations without any built-in libraries. Matrices are stored using nested lists where each inner list represents one row of the matrix. Nested for loops are used to access every element using row index (i) and column index (j).

Addition and subtraction are performed element by element using:
add[i][j] = A[i][j] + B[i][j]
sub[i][j] = A[i][j] - B[i][j]

Matrix multiplication follows the Row × Column rule. Three loops are used where:
- first loop selects row of first matrix  
- second loop selects column of second matrix  
- third loop performs multiplication and addition

mul[i][j] += A[i][k] * B[k][j]

Transpose is done by interchanging row and column positions using:
transpose[j][i] = A[i][j]

Determinant of 2×2 matrix is calculated using mathematical formula:
|A| = ad − bc  
det = A[0][0]*A[1][1] - A[0][1]*A[1][0]

This logic helps to understand how matrix operations work internally without using NumPy functions.

## 👩‍💻 Author

Tanvi  
BCA (AI & Data Science) Student  
Learning Python, AI, ML & Data Science



