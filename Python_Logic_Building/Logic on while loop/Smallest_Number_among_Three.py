# Python Program to find the Smallest number among three
a= int(input("Enter first number "))
b= int(input("Enter second number "))
c= int(input("Enter third number "))

if a<=b and a<=c:
    print(f"{a} is smallest")
elif b<=a and b<=c:
    print(f"{b} is smallest")
else:
    print(f"{c} is smallest")