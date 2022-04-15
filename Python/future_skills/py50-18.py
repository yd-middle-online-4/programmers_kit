lst = [1,2,3]

def has_duplicates(lst):
    if len(lst) > len(set(lst)):
        return True
    else:
        return False
    
has_duplicates(lst)