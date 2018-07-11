from sys import exit
from textwrap import dedent

from ex45room import Room


class Engine(object):

    def __init__(self, start_room):
        self.start_room = start_room
        self.inventory = []
        self.MAX_INVENTORY_SIZE = 3

    def play(self):
        current_room = self.start_room.opening


class Intro(Room):

    def __init__(self):
        super(Intro, self).__init__()
        self.items = [
            {   
                "name": "photo", 
                "description": "Mom and dad, in front of the old cabin.",
                "taken": False
            }
        ]
        self.exits = [
            {
                "id": 1,
                "name": "Hallway"
            }
        ]


    def enter(self):
        if self.entered is False:
            print(dedent("""
                  The sun hadn't even begun to crest the cedars, but somehow my
                  body knew. Time doesn't wait for a fool to make up their mind.

                  My eyes took in my dim surroundings, faintly illuminated by the
                  deep blue of the fading twilight:

                  the familiar arch of the
                  vaulted ceiling;

                  plastic stars,
                  faded and dim;

                  the walnut dresser
                  littered with framed photos;

                  and my things: boots, a navy blue overcoat,
                  my backpack leaning against the doorway, its top open, empty.
                  """))
            self.entered = True
            self.actions()
        else:
            print(dedent("""
                  My room. Couldn't hurt to take one last look around.
                  """))
            self.actions()


Intro().enter()
