from math import ceil


def solution(progresses, speeds):
    answer = []
    lst = []
    for p, s in zip(progresses, speeds):
        day = ceil((100 - p) / s)  # 걸리는 일수
        if lst and max(lst) < day:  # 더 큰값 나오면 비우고
            answer.append(len(lst))
            lst.clear()
        lst.append(day)  # 더 큰값 추가
    answer.append(len(lst))  # 남은 리스트 갯수도 추가
    return answer


print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
