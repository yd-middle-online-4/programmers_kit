citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort(reverse=True)
    for a,b in enumerate(citations):
        if a>=b:
            return a
    return len(citations)

print(solution(citations))