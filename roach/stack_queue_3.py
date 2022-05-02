from collections import deque

def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    answer = 0
    truck_weights = deque(truck_weights + [weight])
    passed = deque([])
    on_way = deque([])
    position = deque([])
    while len(passed) != n:
        if sum(on_way) + truck_weights[0] <= weight:
            on_way.append(truck_weights.popleft())
            position.append(0)
        
        for i in range(len(position)):
            position[i] += 1
        
        if position[0] == bridge_length:
            passed.append(on_way.popleft())
            position.popleft()
        
        answer += 1
    
    return answer + 1