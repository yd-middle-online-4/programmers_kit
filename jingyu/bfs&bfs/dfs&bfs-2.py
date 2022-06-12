def solution(n,com):
    answer = 0
    v = [False for n in range(n)]
    
    while not all(v):
        v = dfs(v.index(False), com, v)
        answer += 1
    
    return answer

def dfs(n, com, v):
    if not v[n]:
        v[n] = True
        for i in range(len(com)):
            if i == n:
                continue
            if com[n][i] == 1:
                v = dfs(i,com,v)
    return v

print(solution(3,[[1,1,0],[1,1,0],[0,0,1]]))