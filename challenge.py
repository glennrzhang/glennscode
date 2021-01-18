
def frameing_glenns(lst):
    nw_lst_lng = 0
    for word in lst:
        if len(word) > nw_lst_lng:
            nw_lst_lng = len(word)
    st_a_ed = "*"*(nw_lst_lng)
    print("**%s**"%st_a_ed)
    for word in lst:
        print("* %s%s *"%(word,(nw_lst_lng-len(word))*" "))
    print("**%s**"%st_a_ed)



frameing_glenns(["----","Glenn","is","Amazg","----"])
