# This is a game that will ask users to roll a dice

# Loop (All of the process should be in a repetive order)
      # ask: roll the dice?
        # if user enters yes (y):
        #     generate two random numbers
        #     print the random numbers
        # if user enters no (n):
        #     print thank you message
        #     terminate
        # else (if what user enters is neither (y) nor (n)):
        #     print invalid choice


import random
# import random is to tell python to help randomize numbers (integers) whenever we ask it

while True:
    choice = input("Roll the dice? (y/n): ").lower()
# user might enter an upper case of (y) or (n).
# no make it easy, i had to convert user input to lower case, hence the function .lower()
    if choice == "y":
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        print(f"({die_1}, {die_2})")
    elif choice == "n":
        print("Thanks for playing!")
        break
# I inserted break to end the loop after user has selected no (n)
# next is to provide for a situation where user fails to input the right response: yes(y) or no(n).
    else:
        print("Yo! That's an Invalid Choice!")
