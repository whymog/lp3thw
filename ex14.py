from sys import argv

script, user_name, adjective = argv
prompt = f'And {user_name} doth say: '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
All right, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.
Finally, you described yourself as "{adjective}." Nice.
""")
