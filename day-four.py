import random  # Allows us to use random number and choice functions.

# Generate a random integer between 2 and 88.
random_integer = random.randint(2, 88)
print(random_integer)

# Generate a random float between 0 and 1.
random_number_float = random.random()
print(random_number_float)

# Generate a random float between 0 and 9.
random_number_float_large = random.random() * 9
print(random_number_float_large)

# Generate a random float inclusive of both parameters.
random_uniform = random.uniform(2, 8)
print(random_uniform)

# Simulate a coin toss.
random_heads_tails = random.randint(0, 1)
if random_heads_tails == 0:
    print("Heads")
else:
    print("Tails")

# List of states in the order they joined the union.
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
    "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
    "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
    "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
    "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
    "Arizona", "Alaska", "Hawaii"
]

# Access states by index.
print(states_of_america[1])  # Second state: Pennsylvania
print(states_of_america[-1])  # Last state: Hawaii

# Reassign a state.
states_of_america[1] = "Reassigned"
print(states_of_america[1])

# Append a new state to the list.
states_of_america.append("Appending")
print(states_of_america)

# Friends list examples.
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends[0])  # Alice
print(friends[-1])  # Emanuel

# Add a new friend to the list.
friends.append("Anna")
print(friends)

# Extend the list with multiple friends.
friends.extend(["Harry", "Rina"])
print(friends)

# Randomly select a friend who will pay.
friends_paying = random.choice(friends)
print(friends_paying)


# You can put Lists inside other Lists, this becomes something called a "Nested List" or a "2D List". e.g.

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
# The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
# You could also represent the list in 2D format like this:

# ["Cherry", "Apple", "Pear"]
# ["Cucumber", "Kale", "Spinnach"]
