tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

single_quotes = '''
Why the hell would I do this instead?
It doesn't really make sense.
"""
Unless...
"""
Nah.
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(single_quotes)

sentence = "My favorite colors are: \n\t*{}\n\t*{}\n\t*{}\n\t*{}"

print(sentence.format("red", "green", "blue", "yellow"))
