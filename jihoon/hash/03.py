from collections import Counter
from functools import reduce

""" reduce() 내부
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
"""


def solution(clothes):
    answer = 0
    counter = Counter()
    for _, kind in clothes:
        counter[kind] += 1
    result = 1
    # 경우의 수 공식
    for key in counter.keys():
        result = result * (counter[key] + 1)
    # result = reduce(lambda acc, cur: acc * (cur + 1), counter.values(), 1) - 1
    return result - 1


""" 한줄 코드
def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1 
"""

# 의상종류가 3개면 각각의 부위에서 안입는것,첫번째,두번째,세번째 총 4개의 선택이 가능하고
# 부위별로 가능한 선택 수를 곱하면 모든 조합이 나오는데 최소 하나는 입어야 해서 1을 빼야 합니다
# (a + 1)(b + 1)(c + 1) - 1 = (a + b + c) + (ab + bc + ca) + abc


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))  # 3
