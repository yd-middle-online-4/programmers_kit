lst = [1,2,3,4,5,6]

def every_nth(lst, n):
    return lst[n-1::n]

print(every_nth(lst, 2))
print(every_nth(lst, 3))