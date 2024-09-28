# Get player 1's choice
player1_choice = input("Player 1, enter your choice (Rock, Paper, or Scissors): ")

# Get player 2's choice
player2_choice = input("Player 2, enter your choice (Rock, Paper, or Scissors): ")

player1_choice = player1_choice.lower()
player2_choice = player2_choice.lower()

# Determine the winner
if player1_choice == player2_choice:
    print("It`s Tie")
elif player1_choice == "rock" and player2_choice == "paper":
    print("Player 2 won the game")
elif player1_choice == "paper" and player2_choice == "rock":
    print("Player 1 won")
elif player1_choice == "rock" and player2_choice == 'scissors':
    print("Player 1 Won")
elif player1_choice == "scissors" and player2_choice == 'rock':
    print("Player 2 Won")
elif player1_choice == "paper" and player2_choice == 'scissors':
    print("Player 2 Won")
else:
    print("Player 1 Won")


# in efficient way or in another way

winning_combinations = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

if player1_choice == player2_choice:
    print("It's a tie!")
elif winning_combinations[player1_choice] == player2_choice:
    print("Player 1 won!")
else:
    print("Player 2 won!")