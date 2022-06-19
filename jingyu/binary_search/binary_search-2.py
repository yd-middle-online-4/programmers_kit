def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    low = 0
    high = distance
    answer= 0

    while low <= high:
        mid = (low + high) // 2
        cur,remove = 0,0
        min_d = float('inf')
        
        for i in rocks:
            dis = i - cur
            if dis < mid:
                remove += 1
            else:
                cur = i
                min_d = min(min_d, dis)
                
        if remove > n:
            high = mid - 1
        else:
            answer = min_d
            low = mid + 1
         
    return answer

print(solution(25,[2,14,11,21,17],2))