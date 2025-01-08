# Print

print("Hello, welcome to the band genertor")
lastName = input("What is your last name?: ")
city = input("What city do you live in?: ")
print("Your band name is " + city + lastName)

# Make this into print statements
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# Spliting the print stament into multiple lines
print("Hello World \nHello World \nHello World")

# Concantenating
print("Hello " + "World")

# Inputs
print("My name is Anna")
otherName = input("What is your name? : ")
print("Hello " + otherName)

# Variables
# everything in just 1 line of code.
print(len(input("What is your name?")))
# Split everything into variables.
name = input("What is your name?")
nameLength = len(name)
print(nameLength)

# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.
glass1 = "milk"
glass2 = "juice"

glass3 = glass1
glass1 = glass2
glass2 = glass3


print(glass1)
print(glass2)
