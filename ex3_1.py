# Prints out text
print("I will now count my chickens:")

# Prints the result of 25 + (30 / 6), which is 25 + 5 = 30.
# Note that a decimal is added - 30.0 - probably due to division.
print("Hens", 25 + 30 / 6)

# Prints the result of 100 - ((25 * 3) % 4),
# which is 100 - (75 % 4),
# which is 100 - 3,
# which is 97.
print("Roosters", 100 - 25 * 3 % 4)

# More text.
print("Now I will count the eggs:")

# PEMDAS, yo. Or more accurately:
# P, E, M/D, A/S
# 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# 3 + 2 + 1 - 5 + 0 - 0.25 + 6
# 6 - 5 - 0.25 + 6
# 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)  # => 6.75

# EVEN MORE TEEEXT
print("Is it true that 3 + 2 < 5 - 7?")

# 5 < 2 => False
print(3 + 2 < 5 - 7)

# Prints "What is 3 + 2? 5"
print("What is 3 + 2?", 3 + 2)
# Prints "What is 5 - 7? -2"
print("What is 5 - 7?", 5 - 7)

# Prints text
print("Oh, that's why it's False.")

# Prints text
print("How about some more.")

# Prints "Is it greater? True"
print("Is it greater?", 5 > -2)

# Prints "Is it greater or equal? True"
print("Is it greater or equal?", 5 >= -2)

# Prints "Is it less or equal? False"
print("Is it less or equal?", 5 <= -2)
