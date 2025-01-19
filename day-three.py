# else if

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# If Else
# Comparator Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

if height > 120:
    print(f"Yay! {height} ! You are tall enough to ride the rollercoaster")
else:
    print("You are too short :(")

if height == 119:
    print("Oh no youre 1cm off")
else:
    print("Go ahead")

if height <= 120:
    print("Youre too smoll")
else:
    print("go ahead")

# modulo

print(10 % 3)  # I think its 1

faveNumber = int(input("Whats your fave number?: "))

if faveNumber % 2 == 0:
    print(f"{faveNumber} is even")
else:
    print(f"{faveNumber} is odd")


# Nesting & elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age?: "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age >= 18:
        print("A ticket is £10")
    elif age >= 15 and age < 18:
        print("A ticket is £8")
    else:
        print("Your ticket is £5")
else:
    print("Sorry you have to grow taller before you can ride.")


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket is  $5.")
    elif age <= 18:
        bill = 7
        print("Student ticket is $7.")
    else:
        print("Adult ticket is  $12.")
        bill = 12

    photo = input("Do you want a photo for £3?: ")

    if photo == "y":
        bill += 3

    print(f"Your bill is £{bill}")
else:
    print("Sorry you have to grow taller before you can ride.")


# Day three execerise:
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
else:
    bill += 25
    if pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your total is £{bill}")
