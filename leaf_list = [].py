def tree_generator(size, trunk_x, trunk_y = None):
    for row in range(size):
        print(" "*(size-1-row),"*"*(2*row+1)) 
    if trunk_y is None:
        trunk_y = int(size/3)
    for row in range(trunk_y):
        print(" "*(int(size-1-(trunk_x-1)/2)),"*"*trunk_x)
tree_generator(3, 7)