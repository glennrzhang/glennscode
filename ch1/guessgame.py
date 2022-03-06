from random import randint
from re import L

# input: guess and secret, returns two numbers exact and correct digits
def str_match(guess_i, number_i):
    guess = [0 for i in range(4)]
    number = [0 for i in range(4)]
    for idx in range(len(guess_i)):
        if idx >= 4:
            break
        guess[idx] = guess_i[idx]
    for idx in range(len(number_i)):
        if idx >= 4:
            break
        number[idx] = number_i[idx]

    number_part_1 = number[0]
    number_part_2 = number[1]
    number_part_3 = number[2]
    number_part_4 = number[3]
    guesses = 0
    answer_given = 0
    nearly_correct_numbers = 0
    absolutly_correct_answers = 0
    guess_num_1 = guess[0]
    guess_num_2 = guess[1]
    guess_num_3 = guess[2]
    guess_num_4 = guess[3]
    if number_part_1 == guess_num_1:
        absolutly_correct_answers += 1
        guess_num_1 = 10
        number_part_1 = 11
    if number_part_2 == guess_num_2:
        absolutly_correct_answers += 1
        guess_num_2 = 10
        number_part_2 = 11
    if number_part_3 == guess_num_3:
        absolutly_correct_answers += 1
        guess_num_3 = 10
        number_part_3 = 11
    if number_part_4 == guess_num_4:
        absolutly_correct_answers += 1
        guess_num_4 = 10
        number_part_4 = 11
    if number_part_1 == guess_num_2:
        nearly_correct_numbers += 1
        guess_num_2 = 10
        number_part_1 = 11
    if number_part_1 == guess_num_3:
        nearly_correct_numbers += 1
        guess_num_3 = 10
        number_part_1 = 11
    if number_part_1 == guess_num_4:
        nearly_correct_numbers += 1
        guess_num_4 = 10
        number_part_1 = 11
    if number_part_2 == guess_num_1:
        nearly_correct_numbers += 1
        guess_num_1 = 10
        number_part_2 = 11
    if number_part_2 == guess_num_3:
        nearly_correct_numbers += 1
        guess_num_3 = 10
        number_part_2 = 11
    if number_part_2 == guess_num_4:
        nearly_correct_numbers += 1
        guess_num_4 = 10
        number_part_2 = 11
    if number_part_3 == guess_num_1:
        nearly_correct_numbers += 1
        guess_num_1 = 10
        number_part_3 = 11
    if number_part_3 == guess_num_2:
        nearly_correct_numbers += 1
        guess_num_2 = 10
        number_part_3 = 11
    if number_part_3 == guess_num_4:
        nearly_correct_numbers += 1
        guess_num_4 = 10
        number_part_3 = 11
    if number_part_4 == guess_num_1:
        nearly_correct_numbers += 1
        guess_num_1 = 10
        number_part_4 = 11
    if number_part_4 == guess_num_2:
        nearly_correct_numbers += 1
        guess_num_2 = 10
        number_part_4 = 11
    if number_part_4 == guess_num_3:
        nearly_correct_numbers += 1
        guess_num_3 = 10
        number_part_4 = 11
    return absolutly_correct_answers, nearly_correct_numbers

def glenns_challenge():
    print("Welcome to Glenns crazy Challenges")
    print("the challenge of this month is guess the number")
    print("this number is a 4 digit number:D")
    number = f"{randint(1,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
    answer_given = 0
    guesses = 0
    while True:
        print(f"This is your {guesses} attempt.")
        guess = input("[guess]>")
        if not all(i.isdigit() for i in guess):
            print(f"Quitting the game, the number was {number}")
            break
        guesses += 1

        absolutely_correct_answers, nearly_correct_answers = str_match(guess, number)
        if guess == number:
            print(f"You win with {guesses} guesses!")
            break
        else:
            print("You didnt get it")
            print(f"You have {absolutely_correct_answers} numbers absolutly correct!")
            print(f"You have {nearly_correct_answers} numbers in the wrong place but match the values of the other numbers in the number.")

glenns_challenge()
# 5 , 7