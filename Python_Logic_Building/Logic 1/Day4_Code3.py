# Multiplaction of two Metrices
import numpy as np
A = [[1,5,7],[4,0,2],[6,0,3]]
B = [[5,9,3],[5,6,8],[5,6,3]]



C = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(C)):
    for j in range(0, len(C[0])):
        for k in range(0,len(B)):
            C[i][j] += A[i][k] * B[k][j]


for row in C:
    print(row)


#----------------------------------------------------------------------

# Multiplaction of two Metrices
import numpy as np
A = [[1,5,7],[4,0,2],[6,0,3]]
B = [[5,9,3],[5,6,8],[5,6,3]]

C = np.zeros([len(A),len(B)],int)
for i in range(0,len(C)):
    for j in range(0, len(C[0])):
        for k in range(0,len(B)):
            C[i][j] += A[i][k] * B[k][j]


for row in C:
    print(row)