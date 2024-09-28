import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

print("Welcome to Guess My Number!")
print("I'm thinking of a number between 1 and 100.")
print(number_to_guess)

while True:

    guess = int(input("Enter your Guess "))
    attempts +=1

    if guess > number_to_guess:
        print("Your guess is too high, No worry do it again")
    elif guess < number_to_guess:
        print("Your guess is too low, Let`s do it again")
    else:
        print(f"Congratulations!! your guess is correct, in {attempts} attempt")
        break
