import heapq as h

def solution(operations):
    lst = []
    for i in range(len(operations)):
        if operations[i].startswith('I'):
            a = operations[i].split()
            h.heappush(lst,a[1])
        else:
            a = operations[i].split()
            if len(lst) != 0:
                if a[1] == '-1':
                    lst.remove(min(lst))
                elif a[1] == '1':
                    lst.remove(max(lst))
    if len(lst) == 0:
        return [0,0]
    else:
        return [max(lst),min(lst)]   

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))