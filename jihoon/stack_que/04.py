from collections import deque


def solution(prices):
    answer = []
    que = deque(prices)
    while que:
        price = que.popleft()
        time = 0
        for p in que:
            time += 1
            if price > p:
                break
        answer.append(time)
    return answer


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
print(solution([1, 2, 3, 0, 0]))

"""
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
"""


""" 리스트 답안
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
"""

""" 오답
def solution(prices):
    answer = []
    for i, price in enumerate(prices):
        time = 0
        for p in prices[i + 1 :]:
            if price <= p:
                time += 1
        answer.append(time)
    return answer
"""
