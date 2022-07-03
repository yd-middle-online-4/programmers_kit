from collections import deque

def seps(p):
    l,r = 0,0
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            return p[:i+1], p[i+1:]
        
            
def checker(u):
    stack = deque()
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True if not stack else False           

def solution(p):
    if not p:
        return p
    
    u,v = seps(p)
    
    if checker(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        for pp in u[1:len(u)-1]:
            if pp == '(':
                answer += ')'
            else:
                answer += '('
    return answer

print(solution("(()())()"))