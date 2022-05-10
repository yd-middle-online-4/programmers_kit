#코드 실행했을 떄 알맞은 정답은 나왔지만 16개 테스트 중에서 한개에 실패 결과가 나온다
#어떤 경우에서 실패가 됐는지 알고 싶지만 테스트 케이스를 확인할 수 없어 답답하다. 
"""
def solution(citations):
    citations = sorted(citations, reverse=True)
    length = len(citations)
    for i in range(length):
        if i+1 > citations[i]:
            return (i)
    return
"""


#다른 사람의 풀이와 내 풀이가 크게 다르지 않은것 같은데 아쉽다.
#다행히 문제에 접근하는 방식을 알맞게 이해하고 진행한 것으로 보인다.
"""
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
"""