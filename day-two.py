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
