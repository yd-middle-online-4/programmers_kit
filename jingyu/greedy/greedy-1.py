def solution(n, lost, reserve):
    ans = reserve
    r_rev = list(set(reserve)-set(lost))
    r_lost = list(set(lost)-set(reserve)) 
    for i in range(1,n+1):
        if i in r_lost:
            if i-1 in r_rev:
                r_lost.remove(i)
                r_rev.remove(i-1)
            elif i+1 in r_rev:           
                r_lost.remove(i)
                r_rev.remove(i+1)
    return n-len(r_lost)

print(solution(3,[3],[1]))