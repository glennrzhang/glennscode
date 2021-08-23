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

def draw_any_triangle_that_you_can_imagine(choice,triangle_type,extra_space=0):

    if triangle_type == 0:
        for row in range(choice):
            print(" "*(choice-row-1+extra_space) + "*"*(row*2+1))
    if triangle_type == 1:
        for row in range(choice-1,-1,-1):
            print(" "*(choice-row-1+extra_space) + "*"*(row*2+1))
    

def diamond_printer(choice):
    draw_any_triangle_that_you_can_imagine(choice,0)
    draw_any_triangle_that_you_can_imagine(choice-1,1,1)

                        
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

def parallelogram_type_1_printer(parallelogram_x,parallelogram_y):
    space_counter = parallelogram_y-1
    reapeted_times = 0
    while reapeted_times < parallelogram_y:
        print(" "*space_counter + "*"*parallelogram_x)
        reapeted_times += 1
        space_counter += -1
def parallelogram_type_2_printer(parallelogram_x,parallelogram_y):
    space_counter = 0
    repeated_times = 0
    while repeated_times < parallelogram_y:
        print(" "*space_counter + "*"*parallelogram_x)
        repeated_times += 1
        space_counter +=1


def x_printer(x_size,x_width):
    total_width = x_size-1+x_width
    x_middle_space = total_width-x_width*2
    x_space_on_the_sides = 0
    

    while x_middle_space > 0:
        print(" "*x_space_on_the_sides+"*"*x_width+" "*x_middle_space+"*"*x_width)
        x_space_on_the_sides += 1
        x_middle_space = total_width-x_space_on_the_sides*2-x_width*2
        
    overlapped_parts=x_width*2-(total_width-x_space_on_the_sides*2)
    while overlapped_parts <= x_width:
        print(" "*x_space_on_the_sides+"*"*(x_width*2-overlapped_parts))
        overlapped_parts+=2
        if overlapped_parts <= x_width:
            x_space_on_the_sides+=1 
    
    x_space_on_the_sides += -1
    overlapped_parts=x_width*2-(total_width-x_space_on_the_sides*2)
    while overlapped_parts >= 0:
      print(" "*x_space_on_the_sides+"*"*(x_width*2-overlapped_parts))
      overlapped_parts+= -2
      x_space_on_the_sides += -1
    

    x_middle_space = total_width-x_space_on_the_sides*2-x_width*2
    while x_middle_space <= total_width-x_width*2:
       print(" "*x_space_on_the_sides+"*"*x_width+" "*x_middle_space+"*"*x_width)
       x_space_on_the_sides += -1
       x_middle_space = total_width-x_space_on_the_sides*2-x_width*2

    
    



x_printer(4,3)
