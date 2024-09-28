# Print full Pyramid

num = int(input("Enter the number "))

for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()


def fullPyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(1,2*i):
            print("*",end=" ")
        print()

num = int(input("Enter the number "))
fullPyramid(num)