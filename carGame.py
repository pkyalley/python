gameMessage = (
"""
-----------------------------
Welcome To The Car Test Shop!
-----------------------------

To Begin, type:
"Start" to Start car
"Stop" to stop car
"Quit" to Exit Car Test Game

----------------------------
"""
)
print(gameMessage)

started = False


while True:
    userInput = input("Please enter your option: ").lower()
    if userInput == "start":
        if started:
            print("Car has already started")
        else:
            started = True
            print("Car has now started")
    elif userInput == "stop":
        if not started:
            print("You need to START car before you can stop it!")
        else:
            started = False
            print("Car is stopped")
    elif userInput == "quit":
        print("Exiting Car Test Game now...")
        break
    else:
        print("I don't understand the command")

print(
"""Game has ended
---------------------------
Thank you for Playing. Bye!
---------------------------
"""
)