def start():
    print("""
    * * * * * * * * * * *
    CALL OF THE WILD CHAZ

            v1.0

      by NICK CUMMINGS

     created for LP3THW

    * * * * * * * * * * *
    """)
    print("You are in the lobby of your office.")
    print("Your sources tell you there's a high probability of finding a wild Chaz around these premises today.")
    print("Smiling to yourself, you pat your trusty BACKPACK of tracker supplies and step through the front door.")

    lobby()

def lobby():
    print("\n* * * LOBBY * * *\n")
    print("You're standing in the lobby of your office.")
    print("To the NORTH lies a staircase leading upward.")
    print("To the WEST, a bespectacled man with a beard leans against a bar and stares intently into his beer.")
    print("To the EAST is a room full of empty tables.")

    choice = input("> ")
    if choice.lower() == "west" or choice.lower() == "w":
        print("Nice.")
    else:
        print("nah.")


start()
