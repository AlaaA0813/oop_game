# Cave Escape classes/functions skeletons

class StartingCavern(object):

    def enter(self):
        pass

class Cavern2(object):

    def caveman(self):
        pass

    def enter(self):
        pass

class Cavern3(object):

    def enter(self):
        pass

class Cavern4(object):

    def enter(self):
        pass

class ExitCavern(object):

    def enter(self):
        pass

class Death(object):

    def enter(self):
        pass

class AllCaverns(object):

    chambers = {
    'start_cav': StartingCavern(),
    'cav_2': Cavern2(),
    'cav_3': Cavern3(),
    'cav_4': Cavern4(),
    'exit_cav': ExitCavern()
    }
