from collections import Counter


def solution(participant, completion):
    answer = ""
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    for key, _ in p_counter.items():
        if key in c_counter.keys():
            p_counter[key] -= c_counter[key]
        if p_counter[key] > 0:
            answer = key

    return answer


""" 모범 답안
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""


participant = [
    ["leo", "kiki", "eden"],
    ["marina", "josipa", "nikola", "vinko", "filipa"],
    ["mislav", "stanko", "mislav", "ana"],
]
completion = [
    ["eden", "kiki"],
    ["josipa", "filipa", "marina", "nikola"],
    ["stanko", "ana", "mislav"],
]

print(solution(participant[0], completion[0]))
print(solution(participant[1], completion[1]))
print(solution(participant[2], completion[2]))
