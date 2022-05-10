def solution(citations):
    n = len(citations)
    idxs = [n - i for i in range(n)]
    citations = sorted(citations)
    matched = []
    
    for j in set(citations):
        idx = citations.index(j)
        matched.append(min([idxs[idx],j]))
    return max(matched)
    
"""    
    for j in set(citations):
        idx = citations.index(j)
        matched.append([idxs[idx],j])
        
    for k in range(len(matched)):
        if matched[k][0] <= matched[k][1]:
            return matched[k][0]
"""