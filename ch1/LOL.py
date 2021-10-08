def challenge_1_m():
    z_size = input("how large do u wish ur Z to be?must be larger or equal to 1 >>>")
    z_size_x = int(z_size)
    if z_size_x < 1:
        print("Next time will u please insert a larger number.")
        print("Your computer will crash...")
        print("Error 303 ur computer terminal is offically broken for the time being")
        return 
    z_size_used = z_size_x + 2
    print("#"*z_size_used)
    loop_number = 1
    z________=z_size_used-1
    while loop_number <= z_size_x:
        three_plus_shift_position = z________ - loop_number
        content_of_da_line = [' '] * z_size_used
        content_of_da_line[three_plus_shift_position] = "#"
        print(''.join(content_of_da_line))
        loop_number += 1
    print("#"*z_size_used)

challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()
challenge_1_m()