a = [-1, 3, 4, 5,6, 2, 9, 10]
b = [3,4]

def continous_sequence(numbers):
    x = 0
    l_seq = 0
    new_l_seq = 0
    previous_number = 0
    for i in numbers:
        if x == 0:
            new_l_seq = 1
            if len(numbers) == 1:
                l_seq = 1
        else:
            previous_number = (numbers[x-1])
            if numbers[x] == previous_number + 1:
                new_l_seq += 1
            else:
                new_l_seq = 1
        x += 1
        if l_seq <= new_l_seq:
            l_seq = new_l_seq
    if l_seq == 1 or l_seq == 0:
        return "No continous sequence. "
    return l_seq

assert continous_sequence([]) == "No continous sequence. "
assert continous_sequence([1]) == "No continous sequence. "
assert continous_sequence([1,2]) == 2
assert continous_sequence([1,2,3]) == 3
assert continous_sequence([1,3]) == "No continous sequence. "
assert continous_sequence([-1,1,2,3,4]) == 4
assert continous_sequence([-1,1,2,3,4, 2, 9, 10]) == 4
assert continous_sequence([-1,1,2, 2, 9, 10, 11]) == 3

