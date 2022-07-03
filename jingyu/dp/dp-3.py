# https://dev-note-97.tistory.com/141

def solution(m, n, puddles):
    graph = [[0] * (m+1) for _ in range(n+1)]  
    graph[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j,i] in puddles or [i, j] == [1, 1]:
                continue
            else:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
    return (graph[-1][-1] % 1000000007)

print(solution(4,3,[2,2]))