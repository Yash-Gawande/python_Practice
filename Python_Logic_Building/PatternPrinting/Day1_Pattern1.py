# print the rignt handed half triangle

num = int(input("Enter The number: "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


def pattern1(x):
    for i in range(0,x+1):
        for j in range(0,i):
            print("*",end=" ")
        print()

num = int(input("Enter the number: "))
pattern1(num)

