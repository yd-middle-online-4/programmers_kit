def solution(clothes):
    closet = {}
    for clothe in clothes:
        if clothe[1] in closet:
            closet[clothe[1]] += 1
        else:
            closet[clothe[1]] = 1
            
    answer = 1
    for num in closet.values():
        answer *= num + 1
    return answer - 1