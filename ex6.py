# Defines a variable, types_of_people, and sets it to 10
types_of_people = 10
# Assigns the format string to x
x = f"There are {types_of_people} types of people."

# Assigns a string to a variable named binary
binary = "binary"
# Assigns a string to a variable named do_not
do_not = "don't"
# Assigns a format string to y
y = f"Those who know {binary} and those who {do_not}."

# Prints the format string x
print(x)

# Prints the format string y
print(y)

# Prints a new format string that encapsulates x
print(f"I said: {x}")

# Prints a new format string that encapsulates y
print(f"I also said: '{y}'")

# Defines a variable, hilarious, equal to boolean false
hilarious = False

# Assigns a formattable string to joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints the joke_evaluation string and inserts the value of hilarious into the curly braces
print(joke_evaluation.format(hilarious))

# Assigns the beginning of a string to w
w = "This is the left side of..."

# Assigns the end of a string to e
e = "a string with a right side."

# Concatenates and prints strings w and e
print(w + e)
