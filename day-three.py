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


# #Logical operators
# A and B #Both conditions need to be true
# C or D #Only one condition needs to be true
# not E #The condition must be false


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:  # this can be written like 45 <= age <= 55
        bill = 0
        print("Midlife crisis tickets are free")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_turn = input("Would you like to go left or right?: ")

if first_turn == "left":
    print("Well done you are onto the next stage")
    second_turn = input("Would you like to swim or wait?: ")
    if second_turn == "wait":
        print("Well done you are onto the next stage")
        third_turn = input(
            "Do you want to go through the red, blue or yellow door?: ")
        if third_turn == "yellow":
            print("You win!!!")
        elif third_turn == "blue":
            print("Eaten by beasts. Game Over")
        elif third_turn == "red":
            print("Burned by fire.Game Over.")
        else:
            print("Game Over.")
    elif second_turn == "swim":
        print("Attacked by trout.Game Over")
    else:
        print("You can only wait or swim")
elif first_turn == "right":
    print("You've fallen into a hole. Game Over.")
else:
    print("You can only turn left or right")
