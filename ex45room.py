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
            
            choice = input("> ")
            if int(choice) > 0 and int(choice) < len(items_to_take) - 1:
                # Take that item
                pass
            elif int(choice) == 0:
                # Go back to room description
                pass
            else:
                # Display an error
                pass
