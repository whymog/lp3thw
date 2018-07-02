# imports argv from sys library
from sys import argv

# assigns arguments to script and input_file variables
script, input_file = argv

# defines a function, print_all, which takes a param, f
def print_all(f):
    # prints out the entire file specified in the param
    print(f.read())

# defines a function, rewind, which takes a param, f
def rewind(f):
    # seeks the "head" back to position 0 - the beginning of the file
    f.seek(0)

# defines a function, print_a_line, which takes two params: line_count (counter for which line we're on), and f (for file)
def print_a_line(line_count, f):
    # prints line count and the result of the file's readline() method
    print(line_count, f.readline())

# defines a variable and assigns input_file to it using the open method
current_file = open(input_file)

print("First let's print the whole file:\n")

# prints the whole file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# sets reader head to beginning of file
rewind(current_file)

print("Let's print three lines:")

# defines a variable, current_line, and sets it equal to 1
current_line = 1
# invokes print_a_line function using current_line and current_file as params
print_a_line(current_line, current_file)

# same as above, but for the next line
current_line += 1
print_a_line(current_line, current_file)

# and once again
current_line += 1
print_a_line(current_line, current_file)
