
# Swap Two Variables

def swap_num(a,b):
    c = a
    a = b
    b = c
    
    return a , b

x = int(input("Enter the first number "))
y = int(input("Enter the second number "))


print(f"After swaping the values of {x} and {y} is", swap_num(x,y))

# ---------------------------------------------------------------------------------

# Is number is positive or negative

num = int(input("Enter the Number "))

if num > 0:
    print(f"{num} is Positive number")
elif num < 0:
    print(f"{num} is Negative number")
else:
    print(f"{num} is neutral")