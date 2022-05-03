from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridgeWeight = 0  # 다리 위의 트럭 무게
    waiting = deque(truck_weights)  # 대기 트럭 큐
    bridge = deque([0 for _ in range(bridge_length)])  # 다리 길이만큼 0으로 채운다.

    while len(waiting) or bridgeWeight > 0:  # 대기 트럭이 있거나 이동 중인 트럭이 있는 동안 반복
        removedTruck = bridge.popleft()  # 다리에서 하나 제거
        bridgeWeight -= removedTruck

        if len(waiting) and bridgeWeight + waiting[0] <= weight:  # 새 트럭이 다리에 올라갈 수 있으면
            newTruck = waiting.popleft()
            bridgeWeight += newTruck

            bridge.append(newTruck)  # 대기 트럭에서 하나 빼서 다리에 올림

        else:  # 새 트럭이 다리에 올라갈 수 없으면
            bridge.append(0)  # 오른쪽에 0을 삽입해서 다리 길이 유지

        time += 1
    return time


# bridge_length # 허용 트럭 수
# weight # 총 허용 무게
# truck_weights # 트럭 무게(들)
print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110


""" 케이스 5번 시간 초과
def solution(bridge_length, weight, truck_weights):
    answer = 0

    doing = [0] * bridge_length
    time = 0
    while True:
        if len(doing) == 0:
            break
        time += 1
        doing.pop(0)
        if truck_weights:
            if sum(doing) + truck_weights[0] <= weight:
                doing.append(truck_weights.pop(0))
            else:
                doing.append(0)
    answer = time
    return answer
"""

""" 클래스 활용(제일 빠름)
import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()
"""
