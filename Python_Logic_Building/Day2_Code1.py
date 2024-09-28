
# Reverse the given number
def reversenum(n):
    temp = 0
    while n > 0:
        digit = n % 10
        temp = temp * 10 + digit
        n //= 10
    print(f"The reverse number is {temp}")

n = int(input("Enter a number "))

reversenum(n)
# -------------------------------------------------------------------

# Check Number is Palindrome or Not
def palindrome(n):
    original_number = n
    temp = 0
    while (n > 0):
        digit = n % 10
        temp = temp * 10 + digit
        n //= 10

    if original_number == temp:
        print(f"{original_number} palindrome number ")
    else:
        print(f"{original_number} not a plaindrome number")

x = int(input("Enter a number "))
palindrome(x)

# -*****************------++++++++++++++++++++++++------------************************************************


# String Is palindrome or not

def str_palindrome(text):

    reverse_text = text[::-1]

    if text == reverse_text:
        print("Its Palindrome Text!")
    else:
        print("It`s Not Palindrome Text!")

text = input("Enter the Text ")
str_palindrome(text)