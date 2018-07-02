# defines a new function that takes two parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints the number of cheese (first param)
    print(f"You have {cheese_count} cheeses!")
    # prints the number of boxes of crackers (second param)
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # prints some text
    print("Man that's enough for a party!")
    # prints some more text
    print("Get a blanket.\n")

# prints text
print("We can just give the function numbers directly:")
# passes 20 and 30 as arguments to cheese_and_crackers()
cheese_and_crackers(20, 30)

# prints text
print("OR, we can use variables from our script:")
# defines a variable, amount_of_cheese, and sets it equal to 10
amount_of_cheese = 10
# defines another variable and sets it equal to 50
amount_of_crackers = 50

# passes those two variables as arguments to our function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints text
print("We can even do math inside too:")
# passes two numbers to our function, which are calculated first
cheese_and_crackers(10 + 20, 5 + 6)

# prints text
print("And we can combine the two, variables and math:")
# passes combined variables and math as arguments to function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
