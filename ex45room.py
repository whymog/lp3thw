# I just split this out into a separate file because the exercise called for
# at least one import. So...here we are.

class Room(object):
    def __init__(self):
        self.entered = False
        self.items = []

    def enter(self):
        print("This room hasn't been written yet.")
        print("You need to subclass it and then implement its enter() method.")
        exit(1)

    def try_int_input(self, prompt):
        try:
            int_input = int(input(prompt))
            return int_input
        except:
            return self.try_int_input("Please enter a number.\n> ")

    def actions(self):
        print("\n1. I decided to look around.")
        print("2. Time to move on.")
        choice = input("> ")
        if choice == 1:
            self.list_items()
        elif choice == 2:
            self.list_exits()
        else:
            print("I'm not sure what that meant. Let me try again.")
            self.actions()

    def list_items(self):
        # First, list all items in the room
        print("You see:")
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
                    print("• {}. Take {}".format(counter, item["name"]))
                print("• 0. Don't take anything")
            
            choice = self.try_int_input("> ")
            if choice > 0 and choice < len(items_to_take) - 1:
                # Take that item
                pass
            elif choice == 0:
                # Go back to room description
                pass
            else:
                # Display an error
                pass
