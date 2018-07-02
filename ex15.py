# This line imports the argv library from sys,
# which is used to parse arguments from the
# command line
from sys import argv

# This line assigns arguments to variables
script, filename = argv

# Runs open on `filename` and assigns value
# to `txt`
txt = open(filename)

# Prints "Here's your file " with the file
# name appended
print(f"Here's your file {filename}:")

# Runs the `read` method on our `txt` var
print(txt.read())

# Close the file
txt.close()

# Prints a string
print("Type the filename again:")

# Assigns value to variable file_again
# from user input with prompt "> "
file_again = input("> ")

# Opens a new file from the prompt given
txt_again = open(file_again)

# Prints the text of the file from the
# user input
print(txt_again.read())

# Close the other file
txt_again.close()
