import heapq
def solution(scoville, K):
    
    heapq.heapify(scoville)
    
    cnt = 0
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
            
        low_sco_food = heapq.heappop(scoville)
        low_sco_food2 = heapq.heappop(scoville)
        heapq.heappush(scoville, (low_sco_food + low_sco_food2 * 2))
        cnt += 1  
    return cnt if scoville[0] >= K else -1