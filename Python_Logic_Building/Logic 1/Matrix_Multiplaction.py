# A basic code for matrix input from user
import numpy as np
R = int(input("Enter the number of rows for 1st metrix:"))
C = int(input("Enter the number of columns for 1st metrix:"))

# Initialize matrix
A = []
print("Enter the entries row wise:")

# For user input
for i in range(R):		 # A for loop for row entries
	a =[]
	for j in range(C):	 # A for loop for column entries
		a.append(int(input()))
	A.append(a)



R1 = int(input("Enter the number of rows for 2nd metrix:"))
C1 = int(input("Enter the number of columns for 2nd metrix:"))

# Initialize matrix
B = []
print("Enter the entries row wise:")

# For user input
for i in range(R1):		 # A1 for loop for row entries
	a1 =[]
	for j in range(C1):	 # A1 for loop for column entries
		a1.append(int(input()))
	B.append(a1)



# For printing the 1st matrix
for i in range(R):
	for j in range(C):
		print(A[i][j], end = " ")
	print("")

# For printing the 2nd matrix
for i in range(R1):
	for j in range(C1):
		print(B[i][j], end = " ")
	print()

# Running this condition to check Column of Matrix A is equal to Rows of Matrix B
if A[j] == B[i]:

#------------------------------------------------

    C = np.zeros([len(A),len(B)],int)

#-----------------------------------------------
    for i in range(0,len(C)):
        for j in range(0, len(C[0])):
            for k in range(0,len(B)):
                C[i][j] += A[i][k] * B[k][j]


    for row in C:
        print(row)
else:
    print("Columns of matrix A is not Equals to Rows of Matrix B")