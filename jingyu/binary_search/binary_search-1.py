def solution(n, times):
    answer = 0
    low = min(times)
    high = max(times)*n
    while low <= high:
        mid = (low + high) // 2
        takes = 0
        
        for i in times:
            takes += mid//i 
            if takes >= n:
                break
            
        if takes >= n:
            answer= mid
            high = mid - 1
        elif takes < n:
            low = mid + 1
    
    return answer

print(solution(6,[7,10]))