def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    n = len(participant)
    for i in range(n - 1):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]