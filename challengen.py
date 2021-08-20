from sys import exit
def str_multiplication(c,n):

    return c*n
 
def draw_a_triangle(choice):
    num_1 = 1
    num_2 = 1

    num_3 = int(choice)-num_1

    while num_2 <= int(choice):
        string_1 = str_multiplication(' ',num_3)
        string_2 = str_multiplication('*',num_1)
        print(f"{string_1}{string_2}{string_1}")
        
        num_1 += 2
        num_2 += 1
        num_3 = int(choice)-num_2


                        
def draw_a_christmas_tree(leaf_size,trunk_x,trunk_y):
    draw_a_triangle(leaf_size)
    num_4 = int(leaf_size-int(trunk_x/2))-1
    string_n_1_0 = " "*num_4
    string_n_1_1 = "*"*trunk_x
    string_n_2_0 = f"{string_n_1_0}{string_n_1_1}{string_n_1_0}"
    num_5 = 0
    while num_5 < trunk_y:
        print(string_n_2_0)
        num_5 += 1

draw_a_christmas_tree(10,9,6)
draw_a_christmas_tree(10,1,6)
draw_a_christmas_tree(2,1,6)
draw_a_christmas_tree(6,3,6)