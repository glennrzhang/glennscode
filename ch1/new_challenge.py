from operator import ne
from sys import exit
from random import randint
print("Welcome to Glenns crazy Challenges")
print("the challenge of this month is guess the number")
print("this number is a 4 digit number:D")
number = f"{randint(1,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
guess = input("[guess]>")
guesses = 0
answer_given = 0
nearly_correct_numbers = 0
absolutly_correct_answers = 0
while answer_given == 0:
    if guesses == 0:
        if guess == number:
            print("You got it first try:D")
    else:
        print(f"This is your {guesses} attempt.")
        if guess == number:
            print("You win!")
        else:
            print("You didnt get it")
            if number[0] == guess[0] or number[0] == guess[1] or number[0] == guess[2] or number[0] == guess[3]:
                 nearly_correct_numbers += 1
            elif number[1] == guess[0] or number[1] == guess[1] or number[1] == guess[2] or number[1] == guess[3]:
                nearly_correct_numbers += 1
            elif number[2] == guess[0] or number[2] == guess[1] or number[2] == guess[2] or number[2] == guess[3]:
                nearly_correct_numbers += 1
            elif number[3] == guess[0] or number[3] == guess[1] or number[3] == guess[2] or number[3] == guess[3]:
                nearly_correct_numbers += 1
            elif number[0] == guess[0]:
                absolutly_correct_answers += 1
            elif number[1] == guess[1]:
                absolutly_correct_answers += 1
            elif number[2] == guess[2]:
                absolutly_correct_answers += 1
            elif number[3] == guess[3]:
                absolutly_correct_answers += 1
            print(f"You have {nearly_correct_numbers} numbers that match")
            