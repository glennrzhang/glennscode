used_number_list = []
def number_of_one_hundred_doubles(input_list):
    list_length = len(input_list)
    idx =0 
    while idx < list_length:
        current_number = input_list[idx]
        idx += 1
        if 100 - current_number in input_list[idx:]:
            print(" "+str(current_number)+","+str(100-current_number)) 
random_list = [50,20,70,30,80,10,10]
number_of_one_hundred_doubles(random_list)