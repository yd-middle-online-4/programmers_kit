def solution(numbers):
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        numbers[i] *= 3 
    answer = ''
    for num in sorted(numbers, reverse=True):
        k=-len(num)//3
        answer += num[:2*k]
    
    if answer == '0' * len(numbers):
        return '0'
    else:
        return answer