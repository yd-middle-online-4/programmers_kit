lst1 = [1,2,3]
lst2 = [2,3,4] 

def intersection(a,b):
    return [x for x in a if x in b]

intersection(lst1,lst2)

# 모범답
# def intersection(a,b):
#   return list(set(a) & set(b))