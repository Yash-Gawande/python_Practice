# print the last all patterns with the continue number

n = int(input("Enter the number "))

for i in range(1,n+1):
    for j in range(i):
        if i==0 or j==i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()