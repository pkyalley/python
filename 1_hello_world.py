# print("Hello, World!")

import random
options =("rock", "scissors","papers")
player = None
computer = random.choice(options)

while player not in options:
  print = input("Enter your choice(rock, scissors, papers):")

print("player: {player}")
print("computer: {computer}")

if player == computer:
  print("It is a drawn game!")
elif player== "rock" and computer == "scissors":
  print("You won!")
elif player == "scissors" and computer == "papers":
  print("You won!")
elif player == "papers" and computer == "rock":
  print("You won!")
else:
  print("You Lost your investment")