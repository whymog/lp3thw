# Defines number of cars available
cars = 100

# Defines how many people fit in a car
space_in_a_car = 4.0

# Defines how many drivers there are
drivers = 30

# Defines the number of passengers to be driven
passengers = 90

# Defines how many cars will not be driven based on the number of drivers
cars_not_driven = cars - drivers

# Defines number of cars driven as equal to number of drivers
# (since cars > drivers)
cars_driven = drivers

# Defines the total capacity of all cars that will be driven
carpool_capacity = cars_driven * space_in_a_car

# Defines how many people, on average, will need to be driven in each car to
# serve all passengers
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car")
