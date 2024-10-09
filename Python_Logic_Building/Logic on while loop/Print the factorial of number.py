# print the factorial of number

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
n = int(input("Enter a number "))

if n<0:
    print("Factorial of negative number is not possible")
else:
    print(f"Factorial of {n} is {factorial(n)}")