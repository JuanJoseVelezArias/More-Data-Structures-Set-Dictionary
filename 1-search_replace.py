def search_replace(my_list, search, replace):

    new =  list(map(lambda i: replace if i == search else i, my_list))
    return new