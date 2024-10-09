
# Find the Square root and Cube Root of the number

def Square_root(x):
    return x ** 0.5

def Cube_root(x):
    return (x ** 0.33)

x = int(input("Enter the number "))

print(f"The Square Root of {x} is ",Square_root(x))
print(f"The Cube Root of {x} the is ",Cube_root(x))

# ----------------------------------------------------------------------------------------------


#Calculate the Area of Triangle

def area_of_triangle(r):
    return 2 * 3.142 * (r * r)

r = float(input("Enter The radius of circle "))
print(f"Area of Circle is ",area_of_triangle(r))