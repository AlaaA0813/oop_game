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
        last_scene = self.scene_map.next_scene('finished') # when we call 'finished', the last_scene gets ran.
        while current_scene != last_Scene:
            next_scene_name = current_scene.enter() # make the next_scene be the current_scene
            current_scene = self.scene_map.next_scene(next_scene_name) # make current_scene the next_scene_name
        current_scene.enter() # print out the scene

class Death(Scene):
    trash = [
    "You lost. Game Over",
    "You got got. The game is over.",
    "You got tooken.",
    "You're bad. Game over.",
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
                As you hesitantly cross the rotting bridge, you step on a moldy plank, snapping the bridge in half and falling to your death, deep into the darkness.
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
                    The mutant caveman pounces on top of you and gulps you down in one bite. You're definitely not alive.
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

class LedgeCavern(Scene):
    def enter(self):
        print(dedent("""
            As you maneuver your way through the passage you discover that it leads to a steep ledge.  The drop is dangerously high and at the bottom are dark waters.  On the other side is another ledge leading to another room.  The cave rumbles again.  You see a rope tied to a stalactite hanging on your end of the ledge. You can swing on the rope to the other side, jump across, or dive into the black water.

            Will you swing, jump, or dive?
            """))

        choice == input('I will:\n')

        if choice == lower('SWING'):
            print(dedent("""
                The rope snaps and you plummet into the dark waters.  A large tentacle pulls you deeper and deaper, your spear having no affect on the creature. You drown before being eaten.
                """))
            return 'death'

        elif choice == lower('DIVE'):
            print(dedent("""
                A large tentacle pulls you deeper, your spear having no affect on the creature. You drown before being eaten.
                """))
            return 'death'

        elif choice == lower('JUMP'):
            print(dedent("""
                You give yourself a running start and long jump across the gap barely making it to the other side.  Phew.
                """))
            return 'octopus'

        else:
            print("Try something else.")
            return 'ledge'

class OctopusRoom(Scene):
    def enter(self):
        print(dedent("""
            As you raise your torch you notice the level of water is knee high, flowing heavily to the left and then pouring over a deep waterfall.  To the far right of the room is a rusted metal ladder leading into a dark cellar, perched over the source of water.  If you go straight across the flowing water, there is a small dark crawl space.  Either way, you must enter the water.

            Will you go left, straight, or right?
            """))

        choice == input('I will go:\n')

        if choice == lower('LEFT') or choice == lower('L'):
            print(dedent("""
                As you lean over the lip of the waterfall, you notice movement in the darkness. A tentacle whips out of nowhere, latching on to the top of your head and pulling you down into the depths. You died.
                """))
            return 'death'

        elif choice == lower('STRAIGHT') or choice == lower('FORWARD') or choice == lower('ACROSS'):
            print(dedent("""
                You trudge your way across the flowing water and as you peer into the crawl space, two mutant cavemen snatch you, dragging you into the shadows where they feast on your soul. And you.
                """))
            return 'death'

        elif choice == lower('RIGHT') or choice == lower('R'):
            print(dedent("""
                As you make your way to the ladder, against the current, you hear another screech roar through the caverns.  It sounds close.  A giant octopus emerges from the depths of the waterfall and it looks hangry af.  His tentacles are flailing every which way.  The bohemath octopus leaves you with no option but to attack.  You notice a large glowing crystal on the center of it's round head.  It seems to be the source of it's power..

                What will you do?
                """))

            choice == input('I will:\n')

            if choice == lower('ATTACK') or choice == lower('STAB') or choice == lower('KILL'):
                print(dedent("""
                    You hurdle your spear at the giant octopus, puncturing the crystal,cracking it..  As the octopus succumbs to a fit of rage, the crystal explodes, turning the giant octopus into a smelly pile of mush.
                    """))
                return 'exitcavern'

            else:
                print(dedent("""
                    The massive octopus effortlessly latches on to you with one of it's suction cups and plops you into it's beak. You get eaten alive!  Should've drank your milk.
                    """))
                return 'death'

class ExitCavern(Scene):
    def enter(self):
        print(dedent("""
            When you reach the top of the ladder, you see a hanging rope underneath a small beam of light.  The rope leads to the surface if you climb!

            What will you do?
            """))

        choice == input('I will:\n')

        if choice == lower('CLIMB') or choice == lower('UP') or choice == lower('GO UP'):
            print(dedent("""
                You made it to the surface! The coast is close by with an abandoned sailboat tied to a deck.  Time to get home.  You escaped the cave! Great jerb! You win!
                """))
            return 'finished'
        else:
            print(dedent("""
                After some thought, you decide that the surface isn't right for you anymore.  You will live amongst the mutant cavemen as one of their gross clansmen..You didn't escape the cave.  You lose.
                """))
            return 'death'



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
