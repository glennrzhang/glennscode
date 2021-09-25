
# return merged string
def merge(str1, str2):
    empty_string = ""
    str_len = len(str1)
    for index in range(str_len):
        print(index)
        if str1[index] == "*":
            empty_string += str1[index]
        elif str2[index] == "*":
            empty_string += "*"
        else:
            empty_string += " "
    return empty_string
        

def xprinter(x, y):
    total_width = x + y - 1
    for letter in range(y):
        string1 = " "*letter+"*"*x+" "*(total_width-letter-x)
        string2 = " "*(total_width-letter-x)+"*"*x+" "*letter
        merged_string = merge(string1, string2)
        print(merged_string)




