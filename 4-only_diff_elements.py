def only_diff_elements(set_1, set_2):
    combination = set_1 | set_2 
    combination -= set_1.intersection(set_2)
    
    return combination