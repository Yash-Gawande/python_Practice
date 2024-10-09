num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

if num1 > num2:
    greater = num1
else:
    greater = num2
while (True):

    if((greater%2==0) and (greater%2==0)):
        lcm = greater
        break
    greater+=1
print(f"LCM of {num1} and {num2} is {greater}")