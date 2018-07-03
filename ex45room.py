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
        for item in self.items:
            if (item["taken"] is False):
                print("> A {}: {}".format(item["name"], item["description"]))
        # Next, list take-able items
        for item in self.items:
            counter = 1
            if (item["taken"] is False):
                print("> {}. Take {}".format(counter, item["name"])) 
