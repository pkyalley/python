# # # # # # # Things to note about functions:
# # # # # #     # 1. Functions perform a task
# # # # # #     # 2. Functions return a value

# # # # # # # Mostly, using return in functions helps to save a data for furthur use

# # # # # # # A parameter is an inout you define for your function
# # # # # # # An argument is the actual value for a given parameter

# # # # # # # If you are requesting for input from users,
# # # # # #     # 1. The parameters also used as the argument
# # # # # #     # 2. Always call the same parameters as argument at the end

# # # # # # # If you use multiple ** infront of a parameter, you are able to pass multiple arguments and make it a dict

# # # # # # # firstName = input("What is your first name?: ")
# # # # # # # lastName = input("What is your last name?: ")

# # # # # # # def greet(firstName, lastName):
# # # # # # #     firstName = firstName.title()
# # # # # # #     lastName = lastName.title()
# # # # # # #     return (
# # # # # # # f"""
# # # # # # # ------------------------------------------------------
# # # # # # # Hey, {firstName}, we will be calling you Mr.{lastName}
# # # # # # # ------------------------------------------------------
# # # # # # # Registration complete, good bye!

# # # # # # # """
# # # # # # #     )
    
# # # # # # # message = greet(firstName, lastName)
# # # # # # # print(message)

# # # # # # # file = open("userRegistration.txt", "w")
# # # # # # # file.write(message)

# # # # # # # def saveUser(**user):
# # # # # # #     print(user)

# # # # # # # saveUser(id = 1, name = "Prince Peter Yalley", age = 29)

# # # # # # # # input = input("What is the magic number?: ")

# # # # # # # def fizz_buzz(input):
# # # # # # #     if (input % 3 == 0) and (input % 5 == 0):
# # # # # # #         return "FizzBuzz"
     
# # # # # # #     if input % 3 == 0:
# # # # # # #         return "Fizz"
# # # # # # #     if input % 5 == 0:
# # # # # # #         return "Buzz"
   
# # # # # # #     return input
    

# # # # # # # print(fizz_buzz(5))

# # # # # # # marks = [55, 64, 75, 80, 65]

# # # # # # # for mark in marks:
# # # # # # #     totalMarks = sum(marks)
# # # # # # #     avgMark = totalMarks / len(marks)

# # # # # # # print(avgMark)

# # # # # # # def grade():
# # # # # # #     if avgMark >= 80:
# # # # # # #         return ("You scored A")
# # # # # # #     if avgMark >= 60 and avgMark <= 80:
# # # # # # #         return ("You scored B")
# # # # # # #     if avgMark >= 50 and avgMark <= 60:
# # # # # # #         return ("You scored C")
# # # # # # #     if avgMark < 50:
# # # # # # #         return ("You scored F")
    
# # # # # # # print(grade())

# # # # # # # def addNumbers(number1, number2):
# # # # # # #     totalNumber = number1 + number2
# # # # # # #     return totalNumber

# # # # # # # task1 = addNumbers(3, 6)
# # # # # # # print(task1)

# # # # # # # def multiplyNumbers(number1, number2):
# # # # # # #     totalNumber = number1 * number2
# # # # # # #     return totalNumber

# # # # # # # task2 = multiplyNumbers(3, 6)
# # # # # # # print(task2)

# # # # # # # nums = [2, 4, 5, 6, 7, 12, 31, 45]

# # # # # # # for num in nums:
# # # # # # #     if num > 12:
# # # # # # #         print(f"{num} is > 12")
# # # # # # #     else:
# # # # # # #         print(f"{num} is not > 12")


# # # # # # users = {"123" : "Prince", "234" : "Yalley", "345" : "Yalley"}

# # # # # # for uid, name in users.items():
# # # # # #     print(uid, name)

# # # # # # ml = ["red", "green", "blue", "yellow"]
# # # # # # vals = ml[0:1]
# # # # # # ml.append("sE")
# # # # # # print(vals)
# # # # # # print(ml)

# # # # # s = "mercury-venus-earth-mars"
# # # # # s_splitted = s.split("-")
# # # # # p = s_splitted[2]

# # # # # print(p)

# # # # # s = "mercury-venus-earth-mars"
# # # # # p = s.split("-")[2]
# # # # # print(p)

# # # # # ds = "2018-10-23"
# # # # # ds = ds.split("-")

# # # # # print(ds[1])

# # # # # zips = {"j":"1", "f":"2", "g":"3", "h":"4"}
# # # # # if zips["f"] == "2":
# # # # #     zips["g"] = "0"
# # # # # else:
# # # # #     zips["b"] = "0"
# # # # #     zips["b"] = "5"

# # # # # print(len(zips))
# # # # # print(zips)

# # # # # s = "a,b,c"
# # # # # a = s.split("b")

# # # # # for i in a:
# # # # #     print(f"{i} is a child from {a}")
# # # # # print(a)

# # # # # myList = ["red", "green", "blue", "yellow"]
# # # # # n = 0

# # # # # for color in myList:
# # # # #     print(n,color)
# # # # #     n += 1


# # # # # myList2 = [1, 4, "6", "78"]
# # # # # for num in myList2:
# # # # #     print(num)

# # # # # md ={"Tyler": "123"}
# # # # # md["Tyler"] = "124"
# # # # # print(md)

# # # # # mylist = {"red":"990000","green":"009900","blue":"000099"}

# # # # # for color,code in mylist.items():
# # # # #     print(color + "-->" + code)

# # # # command = ""
# # # # started = False
# # # # while True:
# # # #     command = input("> ").lower
# # # #     if command == "start":
# # # #         if started:
# # # #             print("Car is alsready started!")
# # # #         else:
# # # #             started = True
# # # #             print("Car started...")
# # # #         print("car started...")
# # # #     elif command == "stop":
# # # #         if not started :
# # # #             print("Car is already stopped!")
# # # #         else:
# # # #             started = False
# # # #             print("Car stopped") 
# # # #         print("car stopped")
# # # #     elif command == "help":
# # # #         print("""
# # # # start - to start the cat
# # # # stop -  sto the the car
# # # # quit - to quit""")
# # # #     elif command == "quit":
# # # #         break
# # # #     else:
# # # #         print("Sorry, I don't understand the command!")

# # # # fees = 995 
# # # # #for fall semester fee
# # # # fall_total = fees * 13  
# # # # #for spring semester fees
# # # # Spring_fees = fees * 12  
# # # # # one year total
# # # # totals = fall_total + Spring_fees  
# # # # print(f"Totals: {totals}")

# # # # f = open("myfile.txt", "w")
# # # # f.write("My data.")
# # # # f.close()



# # # f = open("myfile.txt", "a")
# # # f.write(
# # # """Line1\n
# # # May we have your email? 
# # # We'll send additional information to support your application process. 
# # # If not, please type N/A; otherwise, provide it below.  
# # # """)
# # # f.close()

# # # f = open("myfile.txt", "r")
# # # s = f.read()
# # # f.close()
# # # print(s)

# # a = "9"
# # b = "4"

# # print(a*b)

# names = ["Prince", "Peter", "Yalley"]
# print(names[1])

# countries = [
#     "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
#     "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
#     "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
#     "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
#     "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)",
#     "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
#     "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
#     "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
#     "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
#     "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea (North)", "Korea (South)", "Kosovo", "Kuwait",
#     "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
#     "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
#     "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (formerly Burma)",
#     "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia (formerly Macedonia)",
#     "Norway", "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
#     "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
#     "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone",
#     "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka",
#     "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo",
#     "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
#     "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen",
#     "Zambia", "Zimbabwe"
# ]

# # n = 0

# # for country in countries:
    
# #     print(f"{country} is number {n} as an index")
# #     n += 1
# import random

# names_string = "Prince, Yalley, Abigail"

# names = names_string.split(", ")
# print(names)

# names_length = len(names)

# payer = random.randint(0, names_length - 1)

# print(f"{names[payer]} must pay the bills for today")

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? (e.g., A1, B2): ") # Where do you want to put the treasure?
 # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower()
abc = ["a", "b", "c"]

letter_index = abc.index(letter)
number_index = int(position[1]) - 1

map[number_index][letter_index] = "x"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

# or

# Convert position to row and column indices
row = ord(position[0].upper()) - ord('A')
col = int(position[1]) - 1

# Place the treasure
map[row][col] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")