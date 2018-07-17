# I just split this out into a separate file because the exercise called for
# at least one import. So...here we are.

class Room(object):
    def __init__(self):
        self.entered = False
        self.items = []
        self.exits = []

    def enter(self):
        print("This room hasn't been written yet.")
        print("You need to subclass it and then implement its enter() method.")
        exit(1)

    def try_int_input(self, prompt):
        try:
            int_input = int(input(prompt))
            return int_input
        except ValueError:
            return self.try_int_input("Please enter a number.\n> ")

    def actions(self):
        print("1. I decided to look around.")
        print("2. Time to move on.")
        choice = self.try_int_input("> ")
        if choice == 1:
            self.list_items()
        elif choice == 2:
            self.list_exits()
        else:
            print("Wait, that's not what I did. Let me think...")
            self.actions()

    def list_items(self):
        # First, list all items in the room
        print("\nI saw:\n")
        if (len(self.items) < 1):
            print("Nothing of note.")
        else:
            items_to_take = []
            
            for item in self.items:
                if (item["taken"] is False):
                    print("> A {}: {}".format(item["name"], item["description"]))
            
            # Next, list take-able items
            for item in self.items:
                counter = 1
                if (item["taken"] is False):
                    items_to_take.append(item)
                    print("{}. Take {}".format(counter, item["name"]))
                print("0. I didn't take anything")
            
            choice = self.try_int_input("> ")

            if choice > 0 and choice - 1 < len(items_to_take):
                # Take that item
                print("I took the {}.".format(items_to_take[choice - 1]["name"]))
            elif choice == 0:
                # Go back to room description
                self.enter()
            else:
                # Display an error
                print("Didn't quite get that, sorry.")
                self.list_items()

    def list_exits(self):
        print("From here, I moved to:")
        for exit in self.exits:
            print("{}. {}".format(exit["id"], exit["name"]))
        print("0. On second thought, I wasn't done here just yet.")

        choice = self.try_int_input("> ") 
        
        if choice > 0 and choice - 1 < len(self.exits):
            # Go to that room
            pass
        elif choice == 0:
            # Go back to room description
            self.enter()
        else:
            # Display an error
            print("Wait, that's not what I did.")
            self.list_exits()
