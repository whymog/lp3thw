name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
height_cm = height * 2.54
weight = 180  # lbs
weight_kg = weight * 0.4536
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"In the metric system, I'm {height_cm}cm tall and {weight_kg}kg heavy.")
