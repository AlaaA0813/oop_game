# Learn Python the Hard Way - Zed Shaw
    # Exercise 43, pages 164 - 177
        # Using class skeleton and code to build my game.

# Cave Escape classes/functions skeletons

class Scene(object):

    def enter(self):
        pass

class Progress(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class WoodBridgeChamber(object):

    def enter(self):
        pass

class MutantRoom(object):

    def caveman(self):
        pass

    def enter(self):
        pass

class LedgeCavern(object):

    def enter(self):
        pass

class OctopusRoom(object):

    def enter(self):
        pass

class ExitCavern(object):

    def enter(self):
        pass

class CaveSystem(object):

    def __init__(self, start_game):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


    chambers = {
    'bridges': WoodBridgeChamber(),
    'mutant': MutantRoom(),
    'ledge': LedgeCavern(),
    'octopus': OctopusRoom(),
    'exitcavern': ExitCavern()
    }
