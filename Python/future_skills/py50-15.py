lst = [1,2,2,3,4,4,5]

def filter_unique(lst):
    unique = list(set(lst))
    for i in unique:
        if lst.count(i) < 2:
            lst.remove(i)
    return list(set(lst))
filter_unique(lst)