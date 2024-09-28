# Grade Calculator

# Ask the user to input their scores
name = input("Enter your name ")
math_score = float(input("Enter your Math score: "))
science_score = float(input("Enter your Science score: "))
english_score = float(input("Enter your English score: "))

# Calculate the average score
average_score = (math_score + science_score + english_score) / 3

# Determine the grade
# ... (your code goes here)
"""
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: below 60
"""
if 90<= average_score <= 100:
    print(f"Hey! Congrulations {name} you`ve Got the A Grade")

elif 80<= average_score <=89:
    print(f"Hi! Congrulations {name} you`ve got the B Grade")
elif 70<=average_score<=79:
    print(f"Very Good {name} you`ve got the C Grade")
elif 60<=average_score<=69:
    print(f"Good {name} you`ve Got the D Grade")
else:
    print(f"{name} you`ve got the F grade, Try Harder next time")

#-----------------------------------------------------

""" Here is the another solution in less lines """

# # Calculate the overall average
# average_score = (math_score + science_score + english_score) / 3
#
# # Determine the grade
# grades = {
#     "A": (90, 100),
#     "B": (80, 89),
#     "C": (70, 79),
#     "D": (60, 69),s
#     "F": (0, 59)
# }
#
# for grade, (lower, upper) in grades.items():
#     if lower <= average_score <= upper:
#         print(f"Hey! Congratulations {name} you've got the {grade} Grade")
#         break

#-------------------------------------------------------------------------------------------------

# Time complexity: O(1) - The code has a constant number of operations, regardless of the input size.
# Space complexity: O(1) - The code uses a constant amount of space to store the input variables and the average score.
# The complexity of your code is very good, as it is simple and efficient.