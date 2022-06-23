def solution(n):
    lst = ['1','2','4']
    answer = ''
    
    while n>0:
        n -= 1
        answer = lst[n%3] + answer
        n //= 3
    return answer

print(solution(6))