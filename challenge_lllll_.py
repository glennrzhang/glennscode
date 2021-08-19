
def get_sum_2(list_of_numbers):

    list_of_pairs_that_equal_100 = []
    num_1 = 0
    num_2 = 0
    num_3 = 0
    total_length = len(list_of_numbers)
    while num_3 < total_length:
        num_1 = 0 + num_3
        num_2 = 1  + num_3
        while num_2 < total_length:
            if list_of_numbers[num_1] + list_of_numbers[num_2] == 100:
                list_of_pairs_that_equal_100.append([list_of_numbers[num_1],list_of_numbers[num_2]])
            num_2 +=1
        num_3 += 1
    return list_of_pairs_that_equal_100

list_of_numbers = [1,2,35,5,36,4,65,55,45,3,5,35,24,52,34,52,34]

assert get_sum_2(list_of_numbers) == [[35, 65], [65, 35], [55, 45]]
list_of_numbers = []
assert get_sum_2(list_of_numbers) == []

list_of_numbers = [10,20,30]
assert get_sum_2(list_of_numbers) == []

list_of_numbers = [50]
assert get_sum_2(list_of_numbers) == []

list_of_numbers = [50,50]
assert get_sum_2(list_of_numbers) == [[50,50]]