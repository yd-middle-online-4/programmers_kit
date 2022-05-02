from collections import deque

def solution(prices):
    n = len(prices)
    answer = [0] * (n + 1)
    prices = deque(prices)
    index = deque(range(n))
    p_stack = [[0, n], [prices.popleft(), index.popleft()]]
    while prices:
        for price in p_stack:
            answer[price[1]] += 1
        
        while True:
            if p_stack[-1][0] > prices[0]:
                p_stack.pop()
            else:
                break
        
        p_stack.append([prices.popleft(), index.popleft()])
    
   
    return answer[:-1]