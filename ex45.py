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
