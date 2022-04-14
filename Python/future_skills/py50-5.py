lst = [0, 1, False, 2, '', 3, 'a', 's', 34]

def compact(lst):
    return list(filter(None, lst))

print(compact(lst))

# filter(None, lst 쓰면 None, False, 0, "" 등 제거)