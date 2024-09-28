# print the pyramid of 5 stars

def right_pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("* ",end=" ")
        print()


n = int(input("Number of stars want to print "))
right_pyramid(n)