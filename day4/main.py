import random

userChoose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computerChoose = random.randint(0, 2)

arts = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""",
"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

print(arts[userChoose])
print("Computer chose: ")
print(arts[computerChoose])

if computerChoose == userChoose:
    print("It's a draw")
elif (userChoose == 0 and computerChoose == 2) or (userChoose == 1 and computerChoose == 0) or (userChoose == 2 and computerChoose == 1):
    print("You win!")
else:
    print("You lose")
