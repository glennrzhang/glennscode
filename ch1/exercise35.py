from sys import exit

def gold_room():
    print("This room is full of gold.How much do you take?")

    choice =input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man,learn to type a number.")
    
    if how_much < 50:
        print("Nice,you're not greedy,you win!")
        exit(0)
    else:
        dead("You, greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a lot of honey.")
    print("The fat bear is in front of another door")
    print("How are you gonna move the bear?")
    bear_moved=False
    
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and then slaps your head off.")
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews you leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means")


def cthulhu_room():
    print("Here you see the great evil cthulhu")
    print("He, it, whatever stare at you and you go craxy.")
    print("Do you flee for your life or eat your head?")
    print("while you are thinking about your options you see another room! ")
    print("Do you go inside?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("We'll that was tasty")
    elif:"inside" in choice:
        gold_room()
    else:
        cthulhu_room()ssssss


def dead(why):
    print(why,"Good Job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around and starve to death")






start()