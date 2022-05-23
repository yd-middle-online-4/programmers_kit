def solution(brown, yellow):
    answer = [0,0]
    maxlen = int(yellow**0.5)
    for row in range(1,maxlen+1):
       col = yellow/row
       if (((row+col)*2)+4) == brown:
           answer[0] = int(max(col,row)+2)
           answer[1] = int(min(col,row)+2)
    return answer


print(solution(8,1))