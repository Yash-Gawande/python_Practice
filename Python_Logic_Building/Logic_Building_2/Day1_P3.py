# reverse right-angled triangle

def reverse_right_triangle(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()


n=int(input("Number of stars want to print "))
reverse_right_triangle(n)