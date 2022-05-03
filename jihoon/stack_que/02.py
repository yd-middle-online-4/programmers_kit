def solution(priorities, location):
    answer = 0
    loc = chr(location + 65)
    p = [(p, chr(i + 65)) for i, p in enumerate(priorities)]
    # print(max(p, key=lambda x: x[0]))
    lst = []
    while True:
        if len(p) == 0:
            break
        # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        j = p.pop(0)
        # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
        if p and max(p, key=lambda x: x[0])[0] > j[0]:
            p.append(j)
        # 3. 그렇지 않으면 J를 인쇄합니다.
        else:
            lst.append(j)

    for i, c in enumerate(lst):
        if c[1] == loc:
            answer = i + 1

    return answer


# print([(2, "A"), (1, "B"), (3, "C", (2, "D"))])
print(solution([2, 1, 3, 2], 2))  # 1

# print([(1, "A"), (1, "B"), (9, "C", (1, "D"), (1, "E"), (1, "F"))])
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
