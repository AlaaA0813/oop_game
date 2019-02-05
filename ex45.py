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

class Progress(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene() # current_scene is also the opening_scene
        last_scene = self.scene_map.next_scene('finished') # when we call 'finished', the last_scene gets ranself.
        while current_scene != last_Scene:
            next_scene_name = current_scene.enter() # make the next_scene be the current_scene
            current_scene = self.scene_map.next_scene(next_scene_name) # make current_scene the next_scene_name
        current_scene.enter() # print out the scene

class Death(Scene):
    trash = [
    "You died. Game Over",
    "You got got.",
    "You got tooken.",
    "You died. You're bad.",
    "Looks like you're not escaping.  Game over."
    ] # when you die, one of these strings will appear

    def enter(self):
        print(Death.trash[randint(0, len(self.trash) - 1)]) # from class Death get a random integer ranging from 0(the first string) to the length of trash minus 1 which would return the last string.
        exit(1) # end loop

class WoodBridgeChamber(Scene):
    def enter(self):
        print(dedent("""
            You slowly awaken only to find yourself hanging upside, tied up at your feet.  A torch dimly lights the cavern floors, littered with bones, skulls, a few makeshift wooden tables, and broken chairs.  You're in a cave and the surface is no where in sight.

            You notice a rusty spear just out of arms reach wedged between two rocks, so you swing yourself in range and cut your legs free.  A terrifying screech rips through the caverns as the earth shakes around you.  It's probably best to keep moving.

            You grab the torch and follow a narrow tunnel that splits off into two wooden rope bridges.  One heads left, the other heads right.

            Will you go left or right?
            """))

        choice = input("I will go:\n")

        if choice == lower('LEFT') or choice == lower('L'): # if the user inputs LEFT or L, python will lowercase both and return the following string..
            print(dedent("""
                As you hesitantly cross the rotting bridge, you step on a moldy plank, snapping the bridge in half and falling deep into darkness.
                """))
            return 'death'

        elif choice == lower('RIGHT') or choice == lower('R'): # else if the user inputs RIGHT or L, python will lowercase both and return the following string..
            print(dedent("""
                As you take your last step off of the bridge, the ropes underneath you snap.  It doesn't matter because you made it to the other side. Nice. You dust yourself off.
                """))
            return 'mutant' # go to the next scene

        else:
            print("Try something else.")
            return 'bridges'

class MutantRoom(Scene):
    mutant_alive = True
    def enter(self):
        print(dedent("""
            You get to your feet, raise your torch and notice an enraged mutant caveman.  Behind him is a passageway you can enter to another cavern. Your only way into the passage is through the mutant caveman..

            Will you attack the mutant or enter the passsageway?
            """))

        choice = input('I will:\n')

        while mutant_alive == True:
            if choice == lower('ENTER') or choice == lower('ENTER PASSAGEWAY'):
                print(dedent("""
                    The mutant caveman pounces on top of you and gulps you down in one bite.
                    """))
                return 'death'

            elif choice == lower('ATTACK') or choice == lower('STAB') or choice == lower('KILL'):
                print(dedent("""
                    The mutant caveman begins to charge you and leaps in the air, but before he can reach you, you plunge the spear into it's chest, killing it instantly.
                    """))
                mutant_alive == False
                return 'ledge'

            else:
                print("Try something else.")
                return 'mutant'

class CaveSystem(object):
    scenes = {
    'bridges': WoodBridgeChamber(),
    'mutant': MutantRoom(),
    'ledge': LedgeCavern(),
    'octopus': OctopusRoom(),
    'exitcavern': ExitCavern(),
    'death': Death()
    } # store each scene by name in a dictionary.  use map.scenes to frefer to a name

    def __init__(self, start_game):
        self.start_scene = start_scene # referencing one of the scenes from lines 76-80

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val # get the scene from the dictionary and return that value(val) which is the chosen scene

    def opening_scene(self):
        return self.next_scene(self.start_scene) # this function runs the chosen scene from the value of val

a_map = CaveSystem('bridges')
a_game = Progress(a_map)
a_game.play()
