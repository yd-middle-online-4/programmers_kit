from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()

    return answer


print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]))

# BFS 시도했으나 장렬하게 실패
# def solution(tickets):
#     # 예외 케이스 정리
#     able = set()
#     for i in range(len(tickets)):
#         able.add(tickets[i][0])
    
#     # 초기화
#     q = deque()
#     cand = []
#     V = [False for _ in range(len(tickets))]
#     # 출발지 지정
#     for i in range(len(tickets)):
#         if tickets[i][0] == "ICN":
#             cand.append([tickets[i][1],i])
#     cand.sort()
#     for k in range(len(cand)):
#         if cand[k][0] in able and not q:
#             q.append(tickets[cand[k][1]])
#             V[cand[k][1]] = True
#             break
#     answer = ["ICN",q[0][1]]
    
#     while not all(V):
#         temp_lst = []
#         remain_able = set()
#         frm, to = q.popleft()
#         for i in range(len(tickets)):
#             if not V[i]:
#                 remain_able.add(tickets[i][0])
#                 if to == tickets[i][0]:
#                     temp_lst.append([tickets[i][1],i])
#         temp_lst.sort()
#         for i in range(len(temp_lst)):
#             if temp_lst[i][0] in remain_able:
#                 q.append(tickets[temp_lst[i][1]])
#                 answer.append(temp_lst[i][0])
#                 V[temp_lst[i][1]] = True
#                 break

#     return answer