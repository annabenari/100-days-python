len("Hello")
# Subscripting
print("HELLO"[2])
# String
print("123" + "345")  # This just concatinates the two strings
# Integar = whole number
print(123 + 234)
# large Integar
print(123_234_234)
# Float = Floating point number (decimal point)
print(123.456)
# Boolean = only two values
print(True)
print(False)

# Type
print(type("String"))
print(type(1234))
print(type(123.456))
print(type(True))

# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>

# print("Number of letters in your name: " + len(input("Enter your name"))) --> Comes up with error , cannot concatenate a str and int. The len(input("Enter your name"))) is an int therefore chnage to str.
print("Number of letters in your name: " + str(len(input("Enter your name"))))


# Mathmatical operators
print("My age: " + str(12))
print(1 + 2)
print(1 - 2)
print(6 / 2)  # This division auto comes out as a float e.g. 3.0
print(6 // 2)  # This would make it an Integer e.g. 3
print(1 * 2)
print(1 ** 2)  # To the power of
print(1 // 2)

# Order of Mathematical Operations
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(3 * 3 + 3 / 3 - 3)
print(9 + 3 / 3 - 3)
print(9 + 1 - 3)
print(10 - 3)
print(7)

print(3 * 3 + 3 / 3 - 3)


bmi = 84 / 1.65 ** 2

print(bmi)
# We want a whole number so we can use int
print(int(bmi))
# This comes out and rounds down. We want the nearest whole number which may be different
print(round(bmi))
# Now it comes out with a different number , more accurate the using int

# We can also say how many digits we want to round it to
print(round(bmi, 2))
# This says to two decimal places

# Assignment Operators
score = 0
score = score + 1
# insetad of this we can write it short hand like so
score += 1

# we can do this with
score -= 1
score *= 1
score /= 1


# f-strings
age = 12

print(f"I am {age} years old")

# Will output I am 12 years old.
# This is easier than doing concatinations, we can simply add the vairvle inside the sentence


print(6 + 4 / 2 - (1 * 2))
6+4/2 - (2)
6+2 - 2
