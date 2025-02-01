# Algorithm:

    #   Define Conversion Functions:
        #   fahrenheit_to_celsius(fahrenheit): Converts Fahrenheit to Celsius.
        #   celsius_to_fahrenheit(celsius): Converts Celsius to Fahrenheit.

    #   Prompt User for Choice:
        #   Ask the user to choose between converting Fahrenheit to Celsius ('1') or Celsius to Fahrenheit ('2').

    #   Handle User Input:
        #   If the user chooses '1', prompt for the temperature in Fahrenheit, convert it to Celsius, and print the result.
        #   If the user chooses '2', prompt for the temperature in Celsius, convert it to Fahrenheit, and print the result.
        #   If the user enters an invalid choice, print an error message.

# Code Description:
    #   This script provides a simple temperature conversion tool that allows users to convert temperatures between Fahrenheit and Celsius.
    #   The script defines two functions for the conversions and uses user input to determine which conversion to perform.
    #   The results are formatted and displayed using f-strings.

# Reasons for Using Certain Methods:
    # F-String Formatting:
        # Reason: F-strings provide a concise and readable way to format strings, making the code easier to understand and maintain.
        # Advantages:
        # Readability: F-strings are more readable and concise compared to other string formatting methods.
        # Performance: F-strings are faster than the older % formatting and str.format() method.
        # Modern Syntax: F-strings are a modern feature introduced in Python 3.6, making them the preferred choice for new codebases.

    # Function Definitions:
        # Reason: Defining separate functions for each conversion makes the code modular and reusable.
        # Advantages:
        # Reusability: Functions can be reused in other parts of the program or in different programs.
        # Clarity: Functions encapsulate specific tasks, making the code easier to read and understand.

# This script efficiently handles temperature conversions with clear and concise code, leveraging the advantages of f-strings for formatting and functions for modularity.


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

user_choice = input("Type '1' to convert Fahrenheit to Celsius or '2' to convert Celsius to Fahrenheit: ")

if user_choice == '1':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"Temperature in Celsius is {fahrenheit_to_celsius(fahrenheit):.2f}")

elif user_choice == '2':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"Temperature in Fahrenheit is {celsius_to_fahrenheit(celsius):.2f}")
    
else:
    print("Invalid choice")