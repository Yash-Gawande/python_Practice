# Print the number is armstrong number or not

def armstrong(n):

    # initilize sum
    sum = 0

    # find the sum of the cube
    temp = n

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //=10
    if n == sum:
        print(f"{n}, is Armstrong number ")
    else:
        print(f"{n}, is not Armstrong number ")


num = int(input("Enter the number "))
if __name__ == "__main__":
    print(f"{armstrong(num)}")