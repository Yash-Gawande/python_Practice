# # Find the factorial of the number
import time
n = int(input("Enter the number "))
factorial = 1
if n<0:
    print(f" factorial of {n} dose not exist")
elif n==0:
    print(f"factorial of {n} is 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(f"Factorial of number {n} is {factorial}")


#-------------------------------------------------------------------------------------------


# Python program to find the factorial of a number provided by the user using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
# num = 7

# to take input from the user
num = int(input("Enter a number: "))
init = time.time()
# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)
print(time.time() - init)

#----------------------------------------------------------------------------

# This is the recursive aproach to find the factorial of number
def factoRecur(x):
    if x==1:
        return 1
    else:
        return (x * factoRecur(x - 1))

if __name__ == "__main__":
    num = int(input("Enter the number "))
    print(f"The factorial of {num} is {factoRecur(num)}")

# Iterative approach to find the factorial of a number using function
def factoIter(x):
    factorial = 1
    if x<0:
        print(f"factorial of the {x} is not available because it`s in negative")
    elif x==0:
        print(f"Factorial of the {x} is 1")
    else:
        for i in range(1,x+1):
            factorial = factorial * i
        print(f"The factorial of the {x} is {factorial}")

num = int(input("Enter the number "))
factoIter(num)
