# this gmae will make suers guess a number
# these numbers will be between 1 and 100 probably

# now to the logical sequence

# generate a random number
# ask the user to make a guess
# if not a valid number (that is the number is not between 1 and 100):
#     print error, please try again. number should be between 1 and 100
# if number is less (<) than the guessed
#     print too low
# if number is greater (>) than the guessed
#     print too high
# else (if correct number):
#     print goof job!

#  as usual
    # we need to generate a random number for this game. But this should be only once
    #  we need to make it be in repeat (loop)

import random
# import random is to tell python to help randomize numbers (integers) whenever we ask it

number_to_guess = random.randint(1, 100)


# this is where I introduce the loop (repetiton)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

# Next, I implemented a check to make sure the guess is within range (between 1 and 100)
        if guess < 1 or guess > 100:
            print("Error: Please try again. Number should be between 1 and 100.")
            continue

        if guess < number_to_guess:
            print("Too Low!")
        elif guess > number_to_guess:
            print("Too High!")
        else:
            print("Congratulations! You guessed the right number!")
            break
# I inserted break to end the loop after user has guessed the right number

    except ValueError:
        print("Please enter a valid number")
# what i did up there with the function except valueerror was to provide for a situatio where user fails to enter the right number (between 1 and 100)