score = 0
streak = 0



def start():
    print("Please insert your username")
    
    user_name = input("> ")
    #the part where you create your username
    print("Your quiz started %s"%user_name)
    #the part where it says that question one is going to start
    question_1(score,streak)


def question_1(score,streak):
    print("Question !: In which world war did the nuclear bomb be invented?")
    
    A_1 = input("> ")
    A_1
    if A_1 == "World War 2" or "WW2" or "World war two":
        print("Congrats, you got the correct answer!")
        streak += 1
        score += 100+streak*10
        print("You are on a streak")
        #this is where it says your on a streak
        print(" Your current score is %s "%score)
        #where it tells you where how much score you have
        print(" Your current streak is %s "%streak)
        #this is were it tells you your streak
        question_2(score,streak)
        #it starts question 2
    else:
        print("OOps.The Answer was World War 2")
        #stuff that says like whoops you didnt get the question correct and try better in q 2
        streak = streak-streak
        question_2(score,streak)
        


def question_2(score,streak):  
    print("Question 2: Where nuclear bombs used in world war 1?")
    A_2 = input("> ")
    if A_2 == "No" or "No they werent used in WW1":
        print("Congrats, you got it right.")
        streak += 1
        score += 100+streak*10
        print(f"yer score is {score}")
        #where it tells you where how much score you have
        print(f"Your on a streak. Your current streak is {streak}")
        #this is were it tells you your streak
        question_3(score,streak)
    else:
        print("LMAO, it was invented in WW2, so it could not be used in WW1")
        #stuff that says like whoops you didnt get the question correct and try better in q 3
        
        streak = streak-streak
        question_3(score,streak)
        
def question_3(score,streak):  
    print("Question 3.Now that you know that nucs were used in WW2, what type of nuclear bomb was used in it?")
    A_3 = input("> ")
    if A_3  == " The Atomic Bomb.":
        print("You got it right the Atomic Bomb made by Albert Einstein, you einstein.")
        streak += 1
        score += 100+streak*10
        print(f"Your score is {score}")
        #where it tells you where how much score you have
        print(f"Your on a streak. Your current streak is {streak}")
        #this is were it tells you your streak
        question_4(score,streak)
    else:
        print("The anwser was the Atomic Bomb.")
        #stuff that says like whoops you didnt get the question correct and try better in q 4
        
        streak = streak-streak
        question_4(score,streak)


def question_4(score,streak):  
    print("Question 4.What does NAZI mean?")
    A_4 = input("> ")
    if A_4 == "A member of the National Social Group":
        print("You got it right man.")
        streak += 1
        score += 100+streak*10
        print(f"Your score is {score}")
        #where it tells you where how much score you have
        print(f"Your on a streak. Your current streak is {streak}")
        #this is were it tells you your streak
        question_5(score,streak)
    else:
        print("The anwser was A member of the National Socialist Group")
        #stuff that says like whoops you didnt get the question correct and try better in q 5
        streak = streak-streak
        question_5(score,streak)
        


def question_5(score,streak):  
    print("When did the bombing of pearl habor happen(answer with yyyy/mm/dd)")
    A_5 = input("> ")
    if A_5 == "1914/12/07":
        print("You got it right man, are you a libarian?")
        streak += 1
        score += 100+streak*10
        print(f"Your score is {score}")
        #where it tells you where how much score you have
        print(f"Your on a streak. Your current streak is {streak}")
        #this is were it tells you your streak
        ending(score,streak)
    else:
        print("Better try again later.It was 1914/12/07")
        #stuff that says like whoops you didnt get the question correct 
        ending(score,streak)
        streak =streak-streak


def ending(score,streak):
    print("Your final score is %s and your current streak is %s"%(score,streak))

start()