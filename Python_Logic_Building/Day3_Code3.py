
# Check Leap Year

year = int(input("Enter Year "))

if year % 4 == 0:
    print(f"{year} is Leap year")
else:
    print(f"{year} is not leap year")


# Find the largest Among the 3 numbers

a= int(input("Enter first num"))
b= int(input("Enter second num"))
c= int(input("Enter third num"))

if a > b and b > c:
    print(f"{a} is Greatest number")

elif b > c and c > a:
    print(f"{b} is Greatest number")
elif c > b and b > a:
    print(f"{c} is Greatest")
