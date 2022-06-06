def solution(lst):
    for i in range(1,len(lst)):
        for j in range(i+1):
            if j == 0:
                lst[i][j] = lst[i][j] + lst[i-1][j]
            elif j == i:
                lst[i][j] = lst[i][j] + lst[i-1][j-1]
            else:
                lst[i][j] = max(lst[i][j] + lst[i-1][j],lst[i][j] + lst[i-1][j-1])
    return max(lst[-1])





print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))