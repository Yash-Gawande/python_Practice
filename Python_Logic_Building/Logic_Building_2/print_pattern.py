# if n = 4
# 4444
# 4334
# 4334
# 4444

n = int(input("Enter a number "))
for i in range(n):
    for j in range(n):
        value = max(i,j,n-1-i,n-1-j)+1
        print(value, end="")
    print()
