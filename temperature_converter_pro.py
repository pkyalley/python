# This is an updated version of the initial tempareature_coverter
    # This coverts 
    # Fahrenheit
    # Celsius
    # Kelvin

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

try:
    choice = input("Choose a conversion:\n"
                   "1: Fahrenheit to Celsius\n"
                   "2: Celsius to Fahrenheit\n"
                   "3: Celsius to Kelvin\n"
                   "4: Kelvin to Celsius\n"
                   "5: Kelvin to Fahrenheit\n"
                   "6: Fahrenheit to Kelvin\n")

    if choice == '1':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"Temperature in Celsius is {fahrenheit_to_celsius(f):.2f}")
    elif choice == '2':
        c = float(input("Enter temperature in Celsius: "))
        print(f"Temperature in Fahrenheit is {celsius_to_fahrenheit(c):.2f}")
    elif choice == '3':
        c = float(input("Enter temperature in Celsius: "))
        print(f"Temperature in Kelvin is {celsius_to_kelvin(c):.2f}")
    elif choice == '4':
        k = float(input("Enter temperature in Kelvin: "))
        print(f"Temperature in Celsius is {kelvin_to_celsius(k):.2f}")
    elif choice == '5':
        k = float(input("Enter temperature in Kelvin: "))
        print(f"Temperature in Fahrenheit is {kelvin_to_fahrenheit(k):.2f}")
    elif choice == '6':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"Temperature in Kelvin is {fahrenheit_to_kelvin(f):.2f}")
    else:
        print("Invalid choice")
except ValueError:
    print("Please enter a valid number.")
