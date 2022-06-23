def solution(s):
    answer = []
    result = ''
    
    if len(s) == 1:
        return 1
    
    for i in range(1,len(s)//2+1):
        cnt = 1
        prev = s[:i]
        
        for j in range(i,len(s),i):
            if s[j:j+i] == prev:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                result += str(cnt) + prev
                prev = s[j:j+i]
                cnt = 1
                
        if cnt == 1:
            cnt = ''
        result += str(cnt) + prev
        answer.append(len(result))
        result = ''
            
    return answer

print(solution('aabbaccc'))
