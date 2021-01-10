from random import randint

score = 0
#your points
streak = 0
#streak is how much q's you anwsered correctly in a row

def start():
    print("                 ")
    user_name = input("> ")
    #the part where you create your username
    print("                 ")
    #the part where it says that question one is going to start
    question_1()


def question_1():
    print("         ")
    A_1 = input("> ")
    A_1
    if A_1 == "         ":
        print("         ")
        streak +=1
        score += 100+streak*10
        print("")
        #this is where it says your on a streak
        print("         ")
        #where it tells you where how much score you have
        print("         ")
        #this is were it tells you your streak
        question_2()
    else:
        print("         ")
        question_2


def question_2():  
    print("         ")
    A_2 = input("> ")
    if A_2 == "         ":
        print("     ")
        if streak == 1:
            print("         ")
            score += 100+streak*10
        else:



