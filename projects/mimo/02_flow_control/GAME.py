
import random
print("Let's play rock, paper, or scirssors")

user = input("Chose rock, paper, or scissors: ").lower()
print(f"User chose: {user}")

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
print(f"Computer chose: {computer}")


# Winning conditions
if (user == "rock" and computer == "scissors" or \
    ( user == "scissors" and computer == "paper" or \
    (user == "paper" and computer == "rock"))):
  winner = "Player"

elif user == computer:
  winner = "Tie"

else:
  winner = "Computer"

if winner == "Player":
  print("You won")
elif winner == "Computer":
  print("Computer won")
else:
  print("It's a tie")

