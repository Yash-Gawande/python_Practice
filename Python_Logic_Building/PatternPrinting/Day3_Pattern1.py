# Print Diamond
import time
n = int(input("Enter the number "))

for i in range(1,n+1):
    # printing spaces
    for j in range(n-i):
        print(" ", end=" ")
    # printing the stars
    for k in range(1,2*i):
        print("*", end=" ")
    print()

# Printing the Lower Triangle

for i in range(n-1, 0, -1):
    # printing spaces
    for j in range(n - i):
        print(" ", end=" ")
    # printing the stars
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()


