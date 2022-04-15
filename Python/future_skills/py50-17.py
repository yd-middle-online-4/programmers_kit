itr = [1,2,3]

def for_each_right(itr, fn):
    for i in itr[::-1]:
        fn(i)

for_each_right(itr, print)