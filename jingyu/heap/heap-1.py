import heapq as h

def solution(scoville, K):
    cnt = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            small1 = h.heappop(scoville)
            small2 = h.heappop(scoville)
            h.heappush(scoville, small1+(small2*2))
            cnt += 1
    return cnt

print(solution([1, 1, 1], 2))