# ODD EVEN PRIME
# ODD and Even 

num = int(input("Enter The number to check Even or Odd "))

if (num%2)==1:
    print(f"Number {num} is Odd number")
else:
    print(f"Number {num} is Even number \n")


# prime number 

num1 = int(input("Enter a number to check prime or not "))

""" Prime number is the number which is divided by itself or by 1"""

if num1 > 1:
    for i in range(2,(num1 //2)+1):
        if (num1 % i)==0:
            print(num1, "is not a prime number")
            break
    else:
        print(num1, "is a prime number")
else:
    print(num1, "is not a prime")