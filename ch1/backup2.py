from random import randint
from re import L
def glenns_challenge():

    print("Welcome to Glenns crazy Challenges")
    print("the challenge of this month is guess the number")
    print("this number is a 4 digit number:D")
    number = f"{randint(1,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
    number_part_1 = number[0]
    number_part_2 = number[1]
    number_part_3 = number[2]
    number_part_4 = number[3]
    guess = input("[guess]>")
    guesses = 0
    answer_given = 0
    nearly_correct_numbers = 0
    absolutly_correct_answers = 0
    while answer_given == 0:
        print(f"This is your {guesses} attempt.")
        if guess == number:
            print("You win!")
            answer_given += 1
        else:
            print("You didnt get it")
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
            print(f"You have {absolutly_correct_answers} numbers absolutly correct!")
            print(f"You have {nearly_correct_numbers} numbers in the wrong place but match the values of the other numbers in the number.")
            print(f"Would you like to continue or quit?")
            quiting = input("[quit:yes or no]>>>")
            if quiting == "yes":
                print(f"The number was {number}")
                answer_given+= 1
            else:
                absolutly_correct_answers = 0
                nearly_correct_numbers = 0
                guess = input("[guess]>>>")
                guesses += 1
                number_part_1 = number[0]
                number_part_2 = number[1]
                number_part_3 = number[2]
                number_part_4 = number[3]

glenns_challenge()
