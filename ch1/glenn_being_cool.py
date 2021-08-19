from random import randint
def loser():
    print("you lost u nub")
    print("Game OVer")
def P_1():
    print("you see a luxurious house with an olympic sized swimming pool and a giant sundeck.")
    print("you got the Idea of venturing inside.")
    print("you find a safe that is really secure.")
    print("You have the dumb idea of breaking into it.")
    A_1 = randint(0,9)randint(0,9)
    print("you see a number lock that would go off in ten tries")
    print("Pls insert yer number.")
    nerdy = input(">>>  ")
    guesses = 0
    if nerdy == A_1:
        print("congrats and stuff you broke thru the first lock")
    else:
        guesses += 1
        if guesses  ==9:
            loser()