random_list = range(100)

def number_of_one_hundred_doubles(input_list):
    for variable in input_list:
        if list_contains_number(input_list, 100-variable):
            print("{1}, {2}" % (variable, 100-variable))

# return True is the input_list contains "number", otherwise False.
def list_contains_number(input_list, number):
    return False

                
number_of_one_hundred_doubles(random_list)

