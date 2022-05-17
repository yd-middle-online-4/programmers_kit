def solution(array, commands):
    answer = []
    for order in commands:
        new_array = array[order[0]-1 : order[1]]
        new_array.sort()
        answer.append(new_array[order[2]-1])
    return (answer)

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)