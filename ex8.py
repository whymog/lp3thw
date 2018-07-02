# Declares a variable named formatter, which is equal to a string with four {}s in it
formatter = "{} {} {} {}"

# Prints "1 2 3 4"
print(formatter.format(1, 2, 3, 4))

# Prints "one two three four"
print(formatter.format("one", "two", "three", "four"))

# Prints "True False False True"
print(formatter.format(True, False, False, True))

# Prints "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}"
print(formatter.format(formatter, formatter, formatter, formatter))

# Prints "Try your Own text here Maybe a poem Or a song about fear"
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

