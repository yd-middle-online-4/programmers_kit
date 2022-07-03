import re
from collections import defaultdict
from math import floor

def solution(str1, str2):
    # 전처리
    str1 = str1.upper()
    str2 = str2.upper()
    words = [str1,str2]
    lst = [[],[]]
    cnt = 0
    c_num = 0
    total = 0
    
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
        
    for word in words:
        for i in range(len(word)-1):
            p = word[i]+word[i+1]
            m = re.findall('[A-Z]',p)
            if len(m) == 2:
                lst[cnt].append(''.join(m))
        cnt += 1
        
    set1 = set(lst[0])
    set2 = set(lst[1])
    
    cross = set1&set2
    both = set1|set2
    
    for combi in lst[0]:
        dict1[combi] += 1
    
    for combi in lst[1]:
        dict2[combi] += 1
    
    for num in cross:
        c_num += min(dict1[num],dict2[num])
        
    for num in both:
        total += max(dict1[num],dict2[num])       
    
    if not c_num and not total:
        return 65536
    elif total == 0:
        return 0
    return floor((c_num/total)*65536)

print(solution('E=M*C^2','e=m*c^2'))