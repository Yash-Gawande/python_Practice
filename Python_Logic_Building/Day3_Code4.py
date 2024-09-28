
# Generate The Random Nunber
import random
a = random.randint(1,1000)
print(a)

# --------------------------------------------------------------
# Display the multiplication Table
num = int(input("Enter a number "))

for i in range(1,11,1):
    print(f"{num} * {i} = ",num*i)

