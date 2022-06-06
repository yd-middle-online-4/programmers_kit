from itertools import permutations

def prime_list(n):
    n = n+1
    sieve = [True] * n
    dict = {}

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:   
            for j in range(i+i, n, i): 
                sieve[j] = False
    for j in range(2, n):
        if sieve[j] == True:
            dict[j] = 0
    return dict

def solution(numbers):
    num_list = sorted(list(numbers), reverse=True)
    answer = []
    real_answer = []
    for i in range(1, len(num_list)+1):
        lst = list(permutations(num_list, i))
        for j in range(len(lst)):
            if lst[j][0] != '0':
                answer.append(int(''.join(lst[j])))
    answer.sort() 
    primes = prime_list(answer[-1])
    for i in range(len(answer)):
        if answer[i] in primes:
            real_answer.append(answer[i])        
    return len(set(real_answer))

print(solution("011"))