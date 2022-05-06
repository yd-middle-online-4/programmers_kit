# https://www.ibric.org/myboard/read.php?Board=news&id=270333
# https://velog.io/@jiffydev/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-89-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-H-Index

def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i in range(len(citations)):
        if i+1 <= citations[i]:
            answer = i+1
    return answer

a = [3, 0, 6, 1, 5]
print(solution(a))

# def solution(citations):
#     lst = []
#     s_c = sorted(citations)
#     mins = max(s_c)
#     for i in range(len(s_c)-1,-1,-1):
#         diff = s_c[i]-len(s_c[i:])
#         if diff >= 0 and diff < mins:
#             mins = diff
#             num = s_c[i]
#     return num