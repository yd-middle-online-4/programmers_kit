lst1 = [1,2,3]
lst2 = [1,2,4]

def difference(a,b) : 
	return list(set(a) - set(b))

print(difference(lst1, lst2))

# list(set(a).difference(b)) 이런 것도 있음