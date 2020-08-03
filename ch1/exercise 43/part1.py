class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def _init_(self,scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass    
    
class Central_Corridor(Scene):

    def enter(self):
        pass

class Laser_Weapon_Armoury(Scene):

    def enter(self):
        pass

class The_Bridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):
    
    def enter(self):
        pass


class Map(object):

    def _init_(self,start_scene):
        pass

    def next_scene(self,scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map("central_corridor")
a_gmae = Engine('a_map')
a_game,play()