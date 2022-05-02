from collections import deque
def solution(priorities, location):
    priorities[location] += 0.1
    target = priorities[location]
    answer = 0
    priorities = deque(priorities)
    tmp = 0
    max_p = 0
    
    while True:
        max_p = max(priorities) // 1
        tmp = priorities.popleft()
        if tmp < max_p:
            priorities.append(tmp)
        else:
            answer += 1
            if tmp == target:
                return answer
            
    
    return answer