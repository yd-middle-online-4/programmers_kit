from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        tmp = []
        for order in orders:
            combi = combinations(sorted(order),c)
            tmp += combi
        
        dict = Counter(tmp)
        
        if len(dict) > 0:
            max_ = max(list(dict.values()))
            
            if max_ >= 2:
                for key_,values_ in dict.items():
                    if values_ == max_:
                        answer.append(''.join(map(str,key_)))
    
    answer = sorted(answer)
    
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))