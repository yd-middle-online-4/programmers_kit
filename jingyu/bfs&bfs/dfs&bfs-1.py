answer= 0

def solution(numbers, target):
    idx = 0
    def dfs(idx, sums):
        global answer
        if idx == (len(numbers)):
            if sums == target:
                answer += 1
            return 
        else:
            dfs(idx+1,sums+numbers[idx])
            dfs(idx+1,sums-numbers[idx])
    dfs(0,0)
    return answer

print(solution([4,1,2,1],4))