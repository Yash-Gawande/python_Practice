# Left Handed Half Triangle

num = int(input("Enter the number: "))
b=0
for i in range(num,0,-1):
    b+=1
    for j in range(1,i+1):
        print("*",end=" ")
    print()




