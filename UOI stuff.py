score = 0
#your points
streak = 0
#streak is how much q's you anwsered correctly in a row


def start():
    print("Please insert your username")
    user_name = input("> ")
    #the part where you create your username
    print("YOur quiz started %s"%user_name)
    #the part where it says that question one is going to start
    question_1()


def question_1():
    print("Question !: In which world war did the nuclear bomb be invented?")
    A_1 = input("> ")
    A_1
    if A_1 == "World War 2" or "WW2" or "World war two":
        print("Congrats, you got the correct answer!")
        streak +=1
        score += 100+streak*10
        print("You are on a streak")
        #this is where it says your on a streak
        print(" Your current score is %s "%score)
        #where it tells you where how much score you have
        print(" Your current streak is %s "%streak)
        #this is were it tells you your streak
        question_2()
        #it starts question 2
    else:
        print("OOps.The Answer was World War 2")
        #stuff that says like whoops you didnt get the question correct and try better in q 2
        question_2()
        streak = streak-streak


def question_2():  
    print("         ")
    A_2 = input("> ")
    if A_2 == "         ":
        print("     ")
        streak += 1
        score += 100+streak*10
        print("         ")
        #where it tells you where how much score you have
        print("         ")
        #this is were it tells you your streak
        question_3()
    else:
        print("         ")
        #stuff that says like whoops you didnt get the question correct and try better in q 3
        question_3()
        streak = streak-streak
        
def question_3():  
    print("         ")
    A_3 = input("> ")
    if A_3 == "         ":
        print("     ")
        streak += 1
        score += 100+streak*10
        print("         ")
        #where it tells you where how much score you have
        print("         ")
        #this is were it tells you your streak
        question_4()
    else:
        print("         ")
        #stuff that says like whoops you didnt get the question correct and try better in q 4
        question_4()
        streak = streak-streak


def question_4():  
    print("         ")
    A_4 = input("> ")
    if A_4 == "         ":
        print("     ")
        streak += 1
        score += 100+streak*10
        print("         ")
        #where it tells you where how much score you have
        print("         ")
        #this is were it tells you your streak
        question_5()
    else:
        print("         ")
        #stuff that says like whoops you didnt get the question correct and try better in q 5
        question_5()
        streak = streak-streak


def question_5():  
    print("         ")
    A_5 = input("> ")
    if A_5 == "         ":
        print("     ")
        streak += 1
        score += 100+streak*10
        print("         ")
        #where it tells you where how much score you have
        print("         ")
        #this is were it tells you your streak
        ending()
    else:
        print("         ")
        #stuff that says like whoops you didnt get the question correct 
        ending()
        streak =streak-streak


def ending():
    print("Your final score is %s and your current streak is %s"%(score,streak))