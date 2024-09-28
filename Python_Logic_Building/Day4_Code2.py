# Print the Fibonacci Sequence
import time
"""
F0 = 0
F1 = 1
 Fn = F(n-1) + F(n-2)

0,1,1,2,3,5,8........
"""

"""

Recursion is very bad in fibonacci sequence it takes very much time
"""


def fiboIter(n):
    preNum = 0
    currNum = 1
    for i in range(1,n):
        prevPrevNum = preNum
        preNum = currNum
        currNum = preNum + prevPrevNum
    return currNum

# def fiboRecur(n):
#     if n==0:
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fiboRecur(n-1) + fiboRecur(n-2)


if __name__ == "__main__":
    num = int(input("Enter a number "))
    init = time.time()
    # print(f"Using Recursion value of fib({num}) is {fiboRecur(num)} ")
    print(f"Using Iteration value of fib({num}) is {fiboIter(num)} ")
    print(f"It took {time.time() - init} seconds")