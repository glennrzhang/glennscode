from sys import exit
from random import randit
from textwrap import dedent
    class Scene(object):
        print("This is a not yet configured scene.")
        print("Subclass it and implent enter().")
        exit(1)


    class Engine(object):

        def _init_(self, scene_map):
            self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_map(next_scene_name)
        
        #reminder:print last scene
        current_scene.enter()

    class Death(Scene):

        quips = [
            "You died ya loser."
            "The only one that is proud of you is your son that you made up and dream about."
            "I have a keyboard that can beat you at this, RPG games and fps games."
        

        ]

        def enter(self):
            print(Death.quips[randint(0, len(self.quips)-1)])
            exit(1)

    class CentralCorridor(Scene):

        def enter(self):
            print[
                '''
                The Gothons of Planet dumbbutt ho me sassy #25 have invaded your ship and destroyed your entire crew. 
                You are the last surviving member and your last mission is to get the neutron destruct bomb form the Weapons Armory,
                put it in the bridge,and blow the ship up after getting into an escape pod.

                You're running down the central corridor to the Weapons Armory when a Gothon jumps out,
                red scaly skin,dark grimy teeth,and an evil clown costume flowing aroundhis hate filled body.
                He's blocking the door to the Armory and is about to pull out a weapon to kill you.

                What do you do?
                Your options hex him, dodge or tell a joke.
                '''
            ]

            action = input(">>> ")

            if action == "hex him!":
                print(dedent("""
                Quick on the draw you yank out your wand from your pockets in your cloak and shout out'Bombara Maximus'.
                But your karma gave out on you and you miss because of his costume that obsucured your sight.
                The Gothon got angry and blasted you to nothingness.
                """))
                return 'death'

            elif action == 'dodge!':
                print(dedent("""
                Like a world class boxer you dodge ,weave, slip and slide right as the Gothon's blaster cranks a laser past your head.
                But in the process you get knocked cold as your head collides with a pillar.
                You only recover in time to see him use his blaster to kill you.
                """))

                return 'death'
            
            elif action =='tell a joke!':
                print(dedent("""
                Luckily for you you heard a gothon tell another gothon a joke that made the gothon laugh so much
                that he could not move.As he could not move you pull out your wand and shout out"Sectunsempera" so it died with big gashes on its face.
                """))
                
                return 'laser_weapon_armory'

            else:
                print("Does not compute  you mutton brain,type in one of the options.")
                return'central corridor'
    class LaserWeaponArmory (Scene):

        def enter(self):
            print(dedent("""
            You roll into the laser weapon armory and find the neutron bomb in a container next to you. 
            There is a keypad lock on the box and code the wrong ten times and it will be locked forever or until someone breaks the container.
            The code is three digits.
            """))
        
        code = f"{randint(1,9)}{randit(1,9)}{randit(1,9)}"
        guess = input("[keypad]>")
        guesses = 0

        while guess !=code and guesses < 10:
            print("bzz")
            guess += 1
            guess = input("[keypad]>")

        
        if guess == code:
            print(dedent("""
            The container opens in a pop and you grab the neutron bomb and run as fast as you can to the bridge where that you have to place it in.
            P.S. You also have to put it into the right spot.
            """))
            return 'the bridge'
        else:
            print(dedent("""YOu hear one last buzz as teh lock makes the bomb and things locked forever and useless.
            You decide to sit there as your ship was destroyed."""))
            return 'death'
        