def in_range(n, start, end=0):
    if end == 0:
        if n in range(0,start):
            return True
        else:
            return False
    elif n in range(start, end):
        return True
    else:
        return False