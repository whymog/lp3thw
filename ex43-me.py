game_state = {  
    'central_gothon_defeated': False
}

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map


    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        print("""
        You arrive in the Central Corridor.
        Standing before you is a GOTHON.
        To the NORTH is the Laser Weapon Armory.
        To the WEST is the Bridge.
        To the EAST is an Escape Pod."
        """)
        action = input("> ")
    
        if action != "GOTHON" and not game_state.central_gothon_defeated:
            print("The Gothon looks irritated. It won't let you pass.")
            self.enter()

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):
    scene_map = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        self.scene_map[self.start_scene].enter()

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
