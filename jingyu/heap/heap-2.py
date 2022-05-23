import heapq as h
    
def solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    heap = []
 
    while i < len(jobs):
        # 현재 시점에서 처리 가능한 작업 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                h.heappush(heap, [j[1],j[0]])
        
        if len(heap) > 0: # 처리할 작업 있는 경우
            cur = h.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간->종료시간까지 시간 계산
            i += 1
        else: # 처리할 작업 없는 경우 다음 시간으로 넘어감
            now += 1
        
    return answer // len(jobs)
    
# def solution(jobs):
#     jobs.sort()
#     cnt = 0
#     heap = []
#     size = len(jobs)
#     while len(jobs) > 0:
#         h.heappush(heap, [jobs[0][1],jobs[0][0]])
#         cnt += heap[0][0]
#         jobs.remove(jobs[0])
#         for i in range(cnt):
#             if i < len(jobs):
#                 if jobs[i][0] <= cnt:
#                     h.heappush(heap, [jobs[i][1],jobs[i][0]])
#                     jobs.remove(jobs[i])
#         while len(heap) > 0:
#             a = h.heappop(heap)
#             cnt += a[0]    
#     return math.floor(cnt/size)


print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
# print(solution([[0, 3], [1, 9], [2, 6]]))