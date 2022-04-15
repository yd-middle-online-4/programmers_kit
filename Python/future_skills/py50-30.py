lst = [{'n':4},{'n':2},{'n':8},{'n':6}]
fn = lambda v:v['n']

def max_by(lst, fn):
	return max(map(fn, lst))

print(max_by(lst, fn))