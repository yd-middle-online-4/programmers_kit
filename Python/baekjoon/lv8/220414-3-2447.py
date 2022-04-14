# 재귀로 하는 건 알겠지만 구현을 모르겠음
# 큰 반복 안에 작은 반복 넣는 것 같음
# 프렉탈 도형 그리는 문제, 분할 
# https://imgzon.tistory.com/37 이게 제일 잘함

import sys
input=sys.stdin.readline

def star(a):
    if a == 3:
        return ['***','* *','***']
    
    arr = star(a//3)
    stars = []
    
    for i in arr:
        stars.append(i*3)
        
    for i in arr:
        stars.append(i+' '*(a//3)+i)
        
    for i in arr:
        stars.append(i*3)
        
    return stars
n = int(input())
print('\n'.join(star(n)))