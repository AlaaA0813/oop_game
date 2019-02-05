# Cave Escape!

    # Learn Python the Hard Way - Zed Shaw
    # Exercise 43, pages 164 - 177
    # Using Shaw's class skeleton and code to help build my game.

from sys import exit # will close an infinity loop
from textwrap import dedent # remove indentation from strings

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1) # end loop

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene() # current_scene is also the opening_scene
        last_scene = self.scene_map.next_scene('finished') # when we call 'finished', the last_scene gets ranself.
        while current_scene != last_Scene:
            next_scene_name = current_scene.enter() # make the next_scene be the current_scene
            current_scene = self.scene_map.next_scene(next_scene_name) # make current_scene the next_scene_name
        current_scene.enter() # print out the map
