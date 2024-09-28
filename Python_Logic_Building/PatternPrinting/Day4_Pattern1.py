# Print the Butternfly pattern

def butterfly(n):
    spaces = 2*n-1
    stars = 0

    for i in range(1,2*n):
        if i<=n:
            spaces -= 2
            stars += 1
        else:
            spaces +=2
            stars -=1
        for j in range(1,stars + 1):
            print("*",end=" ")

        for j in range(1,spaces+1):
            print(" ",end=" ")
        for j in range(1, stars+1):
            if j != n:
                print("*",end=" ")
        print()


num = int(input("Enter the number "))
# butterfly(num)

if __name__ == "__main__":
    print(f"The butterfly pattern for {num} is {butterfly(num)}")