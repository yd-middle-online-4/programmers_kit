def solution(answers):
    p1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt1 = [0,0,0]
    cnt2 = [[0,1],[0,2],[0,3]]
    final = []
    
    for i in range(len(answers)):
        ans = answers[i]
        if ans == p1[i%len(p1)]:
            cnt1[0] += 1
            cnt2[0][0] += 1
        if ans == p2[i%len(p2)]:
            cnt1[1] += 1
            cnt2[1][0] += 1
        if ans == p3[i%len(p3)]:
            cnt1[2] += 1
            cnt2[2][0] += 1
    a = max(cnt1)
    for j in range(3):
        if cnt2[j][0] == a:
            final.append(cnt2[j][1])
    final.sort()
    return final 

print(solution([3,3,2,1,5]))